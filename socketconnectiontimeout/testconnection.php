<?php

namespace console\controllers;

use Yii;
use yii\console\Controller;
use common\models\Agent;

class StatusController extends Controller
{
    private function _print_message($message) {
        echo $message.PHP_EOL;
    }

    public function _test_privileges($db_object) {
        $table_name = "testing_dgElg2165s";
        $db_object->createCommand('CREATE TABLE IF NOT EXISTS '.$table_name.' (a INT NOT NULL AUTO_INCREMENT PRIMARY KEY, b BOOLEAN)')->execute();
        $this->_print_message('  Able to create table '.$table_name);
        $db_object->createCommand('INSERT INTO '.$table_name.'(b) VALUES(true)')->execute();
        $this->_print_message('  Able to insert records into table '.$table_name);
        $db_object->createCommand('SELECT * FROM '.$table_name)->execute();
        $this->_print_message('  Able to retrieve records from table '.$table_name);
        $db_object->createCommand('UPDATE '.$table_name.' SET b = false')->execute();
        $this->_print_message('  Able to update records in table '.$table_name);
        $db_object->createCommand('DELETE FROM '.$table_name)->execute();
        $this->_print_message('  Able to delete records from table '.$table_name);
    }
    public function actionTestConnections() {
        Yii::$app->db->open();
        $this->_print_message("MySql Connected.");
        $this->_test_privileges(Yii::$app->db);

        Yii::$app->bgDb->open();
        $this->_print_message("MySql BgJob Connected.");
        $this->_test_privileges(Yii::$app->bgDb);

        Yii::$app->s3->testConnection();
        $this->_print_message("AWS S3 Connected.");

        Yii::$app->redis->open();
        $this->_print_message("Redis Connected.");
	 $start_time=round(microtime(true) * 1000000);
        Yii::$app->redisLocalCacheConn->open();
	        $end_time=round(microtime(true) * 1000000);
        echo $end_time-$start_time."done";
        $this->_print_message("Redis Local Cache Connected.");

        if (YII_ENV_PROD) {
            Yii::$app->mongodb->open();
            $this->_print_message("MongoDB Connected.");

            Yii::$app->es->ping();
            $this->_print_message("ES Connected.");

            Yii::$app->amqp->getConnection();
            $this->_print_message("AMQP Connected.");

            Yii::$app->dbSlave->open();
            $this->_print_message("MySql DB Slave Connected.");
        }
        return 0;
    }
}

