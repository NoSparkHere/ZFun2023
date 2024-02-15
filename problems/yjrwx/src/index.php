<?php
highlight_file(__FILE__);
error_reporting(0);
class Z{
    public $hello;
    public function __construct(){
        $this->hello = "Welcome to ZFun2023";
    }
    public function __destruct(){
        echo $this->hello;
        echo "<br>";
        echo "Wait?Now is 2024!";
    }
}

class F{
    public $what;
    public function __set($func, $vars){
        unset($this->what->isthis);
    }
}

class u{
    public $kobe;
    public function __toString(){
        $this->kobe->helicopter = "See you again";
        return "Lao da xiang ni le";
    }
}

class n{
    public $key;
    public function __unset($var){
        ($this->key)();
    }
}

class HACKER{
    public $flag;
    public $cmd;
    public function __construct(){
        $this->flag = "I won't tell you my flag unless you found my secret.";
    }
    public function __invoke(){
        system($this->cmd);
    }
}

$welcome = new Z();
$yijianriweixing = $_POST['zfun'];
unserialize($yijianriweixing);
