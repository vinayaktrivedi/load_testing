<?php
class Task extends Threaded
{
    private $id;
    public function __construct($id)
    {
	$this->id = $id;
    }
    public function run()
    {
        /*while(1){
            $this->redis->get("key1000");
        }*/
        $redis=new Redis();
	$this->debug('1');
        try {
                $redis->open('127.0.0.1',6379,100);
        } catch(Exception $e){
                echo $e->getMessage();
        }
	$this->debug('2');
        $start_time=round(microtime(true) * 1000000);
        for ($i=1;$i<2000;++$i) {
            $redis->get("key100");
        }
	$this->debug('3');
        $end_time=round(microtime(true) * 1000000);
        #echo $end_time-$start_time;
	$this->debug('4');
	echo "\n";
    }
	private function debug($message){
		echo '['. $this->id .']' . $message . PHP_EOL;
	}
}
$pool = new Pool(10);
for ($i = 0; $i < 10; ++$i) {
    $pool->submit(new Task($i+1)); 
}

while ($pool->collect());

$pool->shutdown();
?>
