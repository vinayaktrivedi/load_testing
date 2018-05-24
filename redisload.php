<?php
ini_set('default_socket_timeout',-1);
class Task extends Threaded
{
    
    public function __construct()
    {

    }
    public function run()
    {
        /*while(1){
            $this->redis->get("key1000");
        }*/
        $redis=new Redis();
        try {
                $redis->open('127.0.0.1',6379,100);
        } catch(Exception $e){
                echo $e->getMessage();
        }
        $start_time=round(microtime(true) * 1000000);
        for ($i=1;$i<2000;++$i) {
            $redis->get("key100");
        }
        $end_time=round(microtime(true) * 1000000);
        echo $end_time-$start_time;
	echo "\n";
    }
}
$pool = new Pool(10);
for ($i = 0; $i < 10; ++$i) {
    $pool->submit(new Task()); 
}

while ($pool->collect());

$pool->shutdown();
?>
