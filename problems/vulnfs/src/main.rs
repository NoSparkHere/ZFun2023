use std::{net::SocketAddr, path::PathBuf};

use axum::{
    body::Body, extract::Query, http::StatusCode, response::IntoResponse, routing::get, Router,
};
use serde::{Deserialize, Serialize};
use tokio::fs::File;
use tokio_util::io::ReaderStream;

#[tokio::main]
async fn main() {
    let router: Router = Router::new().route("/", get(serve_file));
    serve(router, 8000).await
}

async fn serve(app: Router, port: u16) {
    let addr = SocketAddr::from(([0, 0, 0, 0], port));
    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

#[derive(Debug, Serialize, Deserialize)]
struct RequestParams {
    file_path: Option<String>,
}

async fn serve_file(
    Query(RequestParams { file_path }): Query<RequestParams>,
) -> Result<impl IntoResponse, (StatusCode, &'static str)> {
    let file_path = file_path.unwrap_or_else(|| "".to_string());
    let file_path: PathBuf = format!("{}/{}", std::env::current_dir().unwrap().to_str().unwrap(), file_path).into();

    // if path is a dir, return file list
    if file_path.is_dir() {
        let mut files = tokio::fs::read_dir(&file_path).await.map_err(|_| (StatusCode::NOT_FOUND, "Invalid path"))?;
        let mut body = String::new();
        while let Some(file) = files.next_entry().await.map_err(|_| (StatusCode::NOT_FOUND, "Invalid path"))?
        {
            let file_name = file.file_name().into_string().unwrap();
            body.push_str(&format!("{}\n", file_name));
        }
        return Ok((StatusCode::OK, Body::from(body)));
    }

    // otherwise return the file
    let file = File::open(&file_path).await.map_err(|_| (StatusCode::NOT_FOUND, "File not found"))?;
    let stream = ReaderStream::new(file);
    let body = Body::from_stream(stream);
    Ok((StatusCode::OK, body))
}
