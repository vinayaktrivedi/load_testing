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
        $config = [
          "hosts" => [
            [ "addr" => "127.0.0.1", "port" => 3000 ]]];
        $aerospike=new Aerospike($config);
        if (!$aerospike->isConnected()) {
          echo "Failed to connect to the Aerospike server [{$db->errorno()}]: {$db->error()}\n";
          exit(1);
        }
        
	       echo "success\n";
    }
}
$pool = new Pool(10);
for ($i = 0; $i < 10; ++$i) {
    $pool->submit(new Task()); 
}

while ($pool->collect());

$pool->shutdown();
?>
