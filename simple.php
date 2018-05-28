<?php
      $config = [
          "hosts" => [
            [ "addr" => "127.0.0.1", "port" => 3000 ]]];
        $aerospike=new Aerospike($config);
        if (!$aerospike->isConnected()) {
          echo "Failed to connect to the Aerospike server [{$db->errorno()}]: {$db->error()}\n";
          exit(1);
        }
        $key = $aerospike->initKey("test", "demo", "key100");
        $start_time=round(microtime(true) * 1000000);
        for ($i=1;$i<20000;++$i) {
        	$status = $aerospike->get($key, $record, ["name","age"]);
        }
        $end_time=round(microtime(true) * 1000000);
        echo $start_time-$end_time;
        print_r($record);
        
?>