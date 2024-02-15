<?php

// 获取 POST 请求中的 JSON 数据
$jsonData = file_get_contents("php://input");

// 将 JSON 数据解码为关联数组
$data = json_decode($jsonData, true);

// 检查是否成功解码
if ($data === null) {
    // JSON 解码失败，返回错误响应
    $response = array('success' => false, 'message' => 'Invalid JSON data');
    echo json_encode($response);
    exit;
}

// 检查是否存在 "mark" 字段
if (isset($data['mark'])) {
    // 获取 "mark" 的值
    $mark = $data['mark'];
    if($mark >= 200){
        $file = fopen("./flag", "r");
        $content = fread($file, filesize("./flag"));
        fclose($file);
        // 构建响应数组
        $response = array('success' => true, 'message' => $content);
        // 返回 JSON 响应
        echo json_encode($response);
    } else{
        //$response = array('success' => false, 'result' => 'You have not gotten enough marks');
        $response = array('success' => false, 'message' => 'You have not gotten enough marks');
        echo json_encode($response);
    }
} else {
    // 如果缺少 "mark" 字段，返回错误响应
    $response = array('success' => false, 'message' => 'Missing "mark" field');
    echo json_encode($response);
}

?>


