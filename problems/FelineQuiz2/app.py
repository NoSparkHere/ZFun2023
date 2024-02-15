import base64
import hashlib
from flask import Flask, render_template, request, session, make_response, redirect
import OpenSSL

with open("./cert.pem") as f:
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, f.read())

app = Flask(__name__)

app.secret_key = b"fc773dfb1a7a00a1fe24258b75e86baa63d036d69167126ef2912390d18112e8"

question_configs = [{
    "answers": ["kawaii-gcc", "gcc-hentai"],
    "casefold": False
}, {
    "answers": ["1994"],
    "casefold": False
}, {
    "answers": ["MANUALLY_INITIATED_CRASH"],
    "casefold": False
}, {
    "answers": ["sunshine aquarium", "sunshine水族馆", "sunshine 水族馆"],
    "casefold": True
}, {
    "answers": ["48624233", "av48624233"],
    "casefold": True
}, {
    "answers": ["c[at]"],
    "casefold": False
}]

@app.before_request
def check():
    if request.path.startswith("/static/"):
        return
    if request.args.get("token"):
        try:
            token = request.args.get("token")
            id, sig = token.split(":", 1)
            sig = base64.b64decode(sig, validate=True)
            OpenSSL.crypto.verify(cert, sig, id.encode(), "sha256")
            session["token"] = token
        except Exception:
            session["token"] = None
        return redirect("/")
    if session.get("token") is None:
        return make_response("Token error.", 403)


def sha256(msg: str):
    return hashlib.sha256(msg.encode()).hexdigest()


@app.route("/", methods=["GET", "POST"])
def index():
    token = session.get("token")
    correct_flags = [
        f"ZFun{{{sha256(token+'cd02e3d2aff3e8db')[:16]}}}",
        f"ZFun{{{sha256(token+'21ba1d1cb7db907c')[:16]}}}",
        f"ZFun{{{sha256(token+'36eb4ce3a2872f03')[:16]}}}",
    ]
    ctx = {"answered": False, "correct": 0, "extra": False, "flags": []}

    if request.method == "POST":
        answers = request.form
        flags = []
        correct = [False] * 6

        for i in range(len(question_configs)):
            id = "question" + str(i + 1)
            user_answer = answers[id].casefold() if question_configs[i]["casefold"] else answers[id]

            for correct_answer in question_configs[i]["answers"]:
                correct_answer = correct_answer.casefold() if question_configs[i]["casefold"] else correct_answer
                if user_answer == correct_answer:
                    correct[i] = True

        if correct[:5].count(True) >= 3:
            flags.append(correct_flags[0])
        if correct[:5].count(True) == 5:
            flags.append(correct_flags[1])
        if correct[5]:
            flags.append(correct_flags[2])

        ctx["answered"] = True
        ctx["correct"] = correct.count(True)
        ctx["extra"] = correct[5]
        ctx["flags"] = flags

    return render_template("index.html", ctx=ctx)
