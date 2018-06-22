<?php
$client = new Redis();
$result = $client->connect('/var/run/redis/redis.sock');
var_dump($result);
?>

