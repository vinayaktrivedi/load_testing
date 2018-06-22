<?php

namespace console\controllers;

use Yii;
use yii\console\Controller;
use yii\helpers\Console;
use backend\models\City;
use backend\models\Flag;
use backend\models\Neighbourhood;
use backend\models\Retailer;
use backend\models\Campaign;
use backend\models\TheaCityDetails;
use common\models\disease\Diseases;
use backend\models\DownloadCampaign;
use backend\models\Sms;
use backend\models\Marketplace;
use backend\models\UserRoles;
use common\models\Config;

class ProdTestController extends Controller
{
	public static function check($realValue, $cachedValueFromDatabase, $cachedValue,$table){
			if(json_encode($realValue) == json_encode($cachedValueFromDatabase) && json_encode($cachedValueFromDatabase) == json_encode($cachedValue)) {
				echo "Successful\n";
			}
			else{
				echo "Failed ".$table;
			}
	}
	public function actionTest(){
			static::check(City::findOne(10),City::getOneFromCache(10),City::getOneFromCache(10),'City');
			static::check(Flag::findOne(10),Flag::getOneFromCache(10),Flag::getOneFromCache(10),'Flag');
			static::check(Neighbourhood::findOne(10),Neighbourhood::getOneFromCache(10),Neighbourhood::getOneFromCache(10),'Neighbourhood');
			static::check(Retailer::findOne(10),Retailer::getOneFromCache(10),Retailer::getOneFromCache(10),'Retailer');
			static::check(Campaign::findOne(10),Campaign::getOneFromCache(10),Campaign::getOneFromCache(10),'Campaign');
			static::check(TheaCityDetails::findOne(10),TheaCityDetails::getOneFromCache(10),TheaCityDetails::getOneFromCache(10),'TheaCityDetails');
			static::check(Diseases::findOne(10),Diseases::getOneFromCache(10),Diseases::getOneFromCache(10),'Diseases');
			static::check(DownloadCampaign::findOne(10),DownloadCampaign::getOneFromCache(10),DownloadCampaign::getOneFromCache(10),'DownloadCampaign');
			static::check(Sms::findOne(10),Sms::getOneFromCache(10),Sms::getOneFromCache(10),'Sms');
			static::check(Marketplace::findOne(10),Marketplace::getOneFromCache(10),Marketplace::getOneFromCache(10),'Marketplace');
			static::check(UserRoles::findOne(10),UserRoles::getOneFromCache(10),UserRoles::getOneFromCache(10),'UserRoles');
			static::check(Config::findOne(10),Config::getOneFromCache(10),Config::getOneFromCache(10),'Config');

	}
}
?>
