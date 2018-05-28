 <?php
     $config = [
          "hosts" => [
            [ "addr" => "127.0.0.1", "port" => 3000 ]]];
        $aerospike=new Aerospike($config);
        if (!$aerospike->isConnected()) {
          echo "Failed to connect to the Aerospike server [{$db->errorno()}]: {$db->error()}\n";
          exit(1);
        }
        
           echo "success\n";

?>
