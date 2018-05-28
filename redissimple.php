<?php
 $redis=new Redis();
        try {
                $redis->open('127.0.0.1',6379);
        } catch(Exception $e){
                echo $e->getMessage();
        }
        $start_time=round(microtime(true) * 1000000);
        for ($i=1;$i<2000;++$i) {
            $redis->get("key100");
        }
        $end_time=round(microtime(true) * 1000000);
        echo $end_time-$start_time."done";


        ?>
