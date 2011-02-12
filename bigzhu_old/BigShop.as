package bigzhu_old
{
	import big_component.*;
	
	import flash.events.Event;
	import flash.events.FocusEvent;
	
	import mx.collections.ArrayCollection;
	
	import spark.events.IndexChangeEvent;
	
	public class BigShop extends BigBusiness
	{
		public var shop:Shop ;
		public function BigShop()
		{
			shop=crm.id_main_view.id_retail.id_shop;
			super();
		}
		override public function init_data():void
		{
			shop.id_dingHuoQuDao.id_list.dataProvider=new ArrayCollection([
				{label:"网订(公共服务点)", score:80}, 
				{label:"网订(自有电脑)", score:60}, 
				{label:"网订(无电脑)", score:40}, 
				{label:"电话订货", score:20}, 
			]);
			shop.id_guiTaiXingShi.id_list.dataProvider=new ArrayCollection([
				{label:"卷烟专柜", score:80}, 
				{label:"立式柜台", score:50}, 
				{label:"玻璃柜台", score:50}, 
				{label:"玻璃橱", score:30}, 
				{label:"窗口式", score:20}, 
			]);
			
			shop.id_caiWuNengLi.id_list.dataProvider=new ArrayCollection([
				{label:"差(不记帐)", score:30}, 
				{label:"一般(口头记帐)", score:50}, 
				{label:"好(笔记记帐)", score:80}, 
			]);
			shop.id_dianPuYingLi.id_num.maximum=99999999;
			shop.id_zhouZhuanZiJin.id_num.maximum=99999999;
			shop.id_yueJunXiaoShouLiang.id_num.maximum=99999999;
			shop.id_danTiaoZhi.id_num.maximum=99999999;
			shop.id_danTiaoZhi.id_num.snapInterval=0.1;
		}
		override public function add_all():void
		{
			add_to(shop.id_dianPuWeiZhi);
			add_to(shop.id_dingHuoQuDao);
			add_to(shop.id_guiTaiXingShi);
			add_to(shop.id_jingYingMianJi);
			add_to(shop.id_yingYeShiChang);
			add_to(shop.id_dianPuLeiXing);
			add_to(shop.id_dianPuXingXiang);
			add_to(shop.id_dianPuYingLi);
			add_to(shop.id_zhouZhuanZiJin);
			add_to(shop.id_jiaTIngZhuYaoShouRuLaiYuan);
			add_to(shop.id_faRenXingMing);
			add_to(shop.id_faRenZhiYe);
			add_to(shop.id_jingYingZheShuLinag);
			add_to(shop.id_zhuYaoJingYingZheNianLin);
			add_to(shop.id_zhuYaoJingYingZheJiaoYuChengDu);
			add_to(shop.id_pinPaiPianHao);
			add_to(shop.id_keHuSuQiu);
			add_to(shop.id_jingYingDongJi);
			add_to(shop.id_manYiDu);
			add_to(shop.id_keHuJingLiFuWuZhiXingQingKuang);
			add_to(shop.id_tuiJianNengLi);
			add_to(shop.id_kuCunGuanLiNengLi);
			add_to(shop.id_caiWuNengLi);
			add_to(shop.id_chanPinZuHeNengLi);
			add_to(shop.id_yueJunXiaoShouLiang);
			add_to(shop.id_danTiaoZhi);
			add_to(shop.id_jingYingLiRun);
		}
		override public function show_what():void
		{
			var retail:ComplexRetail;
			
			retail=shop.id_dianPuWeiZhi;
			show_text_input(retail);
			
			retail=shop.id_dingHuoQuDao;
			show_list_bar_text(retail);
			
			retail=shop.id_guiTaiXingShi;
			show_list_bar_text(retail);
			
			retail=shop.id_jingYingMianJi;
			show_num_bar_text(retail);
			
			retail=shop.id_yingYeShiChang;
			show_num_bar_text(retail);
			
			retail=shop.id_dianPuLeiXing;
			show_text_input(retail);
			
			retail=shop.id_jiaTIngZhuYaoShouRuLaiYuan;
			show_text_input(retail);
			
			retail=shop.id_dianPuXingXiang;
			show_num_bar_text(retail);
			
			retail=shop.id_dianPuYingLi;
			show_num_bar_text(retail);
			
			retail=shop.id_zhouZhuanZiJin;
			show_num_bar_text(retail);
			
			retail=shop.id_faRenXingMing;
			show_text_input(retail);
			
			retail=shop.id_faRenZhiYe;
			show_text_input(retail);
			
			retail=shop.id_jingYingZheShuLinag;
			show_num_bar_text(retail);
			
			retail=shop.id_zhuYaoJingYingZheNianLin;
			show_num_bar_text(retail);
			
			retail=shop.id_zhuYaoJingYingZheJiaoYuChengDu;
			show_num_bar_text(retail);
			
			retail=shop.id_pinPaiPianHao;
			show_text_input(retail);
			
			retail=shop.id_keHuSuQiu;
			show_text_input(retail);
			
			retail=shop.id_jingYingDongJi;
			show_num_bar_text(retail);
			
			retail=shop.id_manYiDu;
			show_num_bar_text(retail);
			
			retail=shop.id_keHuJingLiFuWuZhiXingQingKuang;
			show_num_bar_text(retail);
			
			retail=shop.id_tuiJianNengLi;
			show_num_bar_text(retail);
			
			retail=shop.id_kuCunGuanLiNengLi;
			show_num_bar_text(retail);
			
			retail=shop.id_caiWuNengLi;
			show_num_bar_text(retail);
			
			retail=shop.id_chanPinZuHeNengLi;
			show_num_bar_text(retail);
			
			retail=shop.id_yueJunXiaoShouLiang;
			show_num_bar_text(retail);
			
			retail=shop.id_danTiaoZhi;
			show_num_bar_text(retail);
			
			retail=shop.id_jingYingLiRun;
			show_num_bar_text(retail);
		}
		
		override public function add_event():void
		{
			shop.id_dianPuWeiZhi.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			shop.id_dianPuLeiXing.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			shop.id_jiaTIngZhuYaoShouRuLaiYuan .addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			shop.id_faRenXingMing.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			shop.id_faRenZhiYe.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			shop.id_pinPaiPianHao.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			shop.id_keHuSuQiu.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			
			shop.id_dingHuoQuDao.addEventListener(FocusEvent.FOCUS_OUT, just_in_list);
			shop.id_guiTaiXingShi.addEventListener(FocusEvent.FOCUS_OUT, just_in_list);
			
			
			shop.id_dianPuXingXiang.addEventListener(FocusEvent.FOCUS_OUT, BigPublic.setGoodBar);
			shop.id_keHuJingLiFuWuZhiXingQingKuang.addEventListener(FocusEvent.FOCUS_OUT, BigPublic.setGoodBar);
			
			shop.id_jingYingMianJi.addEventListener(FocusEvent.FOCUS_OUT, jingYingMianJi);
			shop.id_yingYeShiChang.addEventListener(FocusEvent.FOCUS_OUT, yingYeShiChang);
			shop.id_jingYingZheShuLinag.addEventListener(FocusEvent.FOCUS_OUT, jingYingZheShuLinag);
			shop.id_zhuYaoJingYingZheNianLin.addEventListener(FocusEvent.FOCUS_OUT, zhuYaoJingYingZheNianLin);
			shop.id_zhuYaoJingYingZheJiaoYuChengDu.addEventListener(FocusEvent.FOCUS_OUT, zhuYaoJingYingZheJiaoYuChengDu);
			shop.id_jingYingDongJi.addEventListener(FocusEvent.FOCUS_OUT, jingYingDongJi);
			shop.id_manYiDu .addEventListener(FocusEvent.FOCUS_OUT, manYiDu);
			shop.id_tuiJianNengLi .addEventListener(FocusEvent.FOCUS_OUT, tuiJianNengLi );
			shop.id_kuCunGuanLiNengLi .addEventListener(FocusEvent.FOCUS_OUT, kuCunGuanLiNengLi);
			shop.id_caiWuNengLi .addEventListener(FocusEvent.FOCUS_OUT, caiWuNengLi );
			shop.id_chanPinZuHeNengLi .addEventListener(FocusEvent.FOCUS_OUT, chanPinZuHeNengLi);
			shop.id_yueJunXiaoShouLiang .addEventListener(FocusEvent.FOCUS_OUT, yueJunXiaoShouLiang);
			shop.id_danTiaoZhi .addEventListener(FocusEvent.FOCUS_OUT, danTiaoZhi );
			shop.id_jingYingLiRun.addEventListener(FocusEvent.FOCUS_OUT, jingYingLiRun);
			
			shop.id_dianPuYingLi.addEventListener(FocusEvent.FOCUS_OUT, dianPuYingLi);
			shop.id_zhouZhuanZiJin.addEventListener(FocusEvent.FOCUS_OUT, zhouZhuanZiJin);
		}
		
		public function jingYingLiRun(event:Event):void
		{
			
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			var score:Number;
			if(num==8)
				score=50;
			if(num<8)
			{
				score=50-(8-num)*10;
				if(score<0)
					score=0;
			}
			if(num>8)
			{
				score=50+(num-8)*5;
				if(score>100)
					score=100;
			}
			retail.score=score;
			
			var value:String;
			value=String(num)+'%';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}
		public function danTiaoZhi(event:Event):void
		{
			
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			var score:Number;
			if(num==53.4)
				score=40;
			if(num<53.4)
			{
				score=40-(53.4-num)/0.5;
				if(score<0)
					score=0;
			}
			if(num>53.4)
			{
				score=40+(num-53.4)/0.5;
				if(score>100)
					score=100;
			}
			retail.score=score;
			
			var value:String;
			value=String(num)+'元/条';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}
		public function yueJunXiaoShouLiang(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			var score:Number;
			if(num==122)
				score=40;
			if(num<122)
			{
				score=40-(122-num)/10;
				if(score<0)
					score=0;
			}
			if(num>122)
			{
				score=40+(num-122)/10;
				if(score>100)
					score=100;
			}
			retail.score=score;
			
			var value:String;
			value=String(num)+'条/月';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}
		
		public function chanPinZuHeNengLi(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			var score:Number;
			if(num==17)
				score=50;
			if(num<17)
			{
				score=50-(17-num)*2;
				if(score<0)
					score=0;
			}
			if(num>17)
			{
				score=50+(num-17)*2;
				if(score>100)
					score=100;
			}
			retail.score=score;
			
			var value:String;
			value=String(num)+'个';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}
		
		public function caiWuNengLi (event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			score=num;
			retail.score=score;
			var value:String;
			if(score<=30)
				value='差:不记账';
			else if(score<50)
				value='一般:口头记账';
			else if(score<=100)
				value='好:笔记记账';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}
		public function tuiJianNengLi (event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			score=num;
			retail.score=score;
			var value:String;
			if(score<=40)
				value='任顾客自行选择';
			else if(score<60)
				value='能够适当引导';
			else if(score<80)
				value='品牌推荐能力';
			else if(score<=100)
				value='批零互动能力';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}	
		public function manYiDu(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			score=num;
			retail.score=score;
			var value:String;
			if(score<=20)
				value='不满意';
			else if(score<40)
				value='不太满意';
			else if(score<60)
				value='一般';
			else if(score<80)
				value='比较满意';
			else if(score<=100)
				value='非常满意';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}	
		public function jingYingDongJi(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			score=num;
			retail.score=score;
			var value:String;
			if(score<=20)
				value='打发时间';
			else if(score<35)
				value='就业';
			else if(score<50)
				value='生计需要';
			else if(score<65)
				value='增加额外收入';
			else if(score<80)
				value='创业发财';
			else if(score<=100)
				value='事业追求';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}	
		public function zhuYaoJingYingZheJiaoYuChengDu(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			score=num;
			retail.score=score;
			
			var value:String;
			if(score<=20)
				value='小学';
			else if(score<35)
				value='初中';
			else if(score<50)
				value='高中(高职、中专)';
			else if(score<65)
				value='大专';
			else if(score<80)
				value='本科';
			else if(score<=100)
				value='硕士研究生及以上';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}
		public function zhuYaoJingYingZheNianLin(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num>=18 && num<=22)
				score=50;
			if(num>=23 && num<=30)
				score=60;
			if(num>=30 && num<=45)
				score=80;
			if(num>=45 && num<=60)
				score=60;
			if(num>60)
				score=40;
			retail.score=score;
			
			var value:String=String(num)+'岁';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);				
		}
		public function zhouZhuanZiJin(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num==10000)
				score=50;
			if(num>10000)
			{
				score=50+Math.round((num-10000)/400);
				if(score>100)
					score=100;
			}
			if(num<10000)
			{
				score=50-Math.round((10000-num)/400);
				if(score<0)
					score=0;
			}
			retail.score=score;
			
			var value:String=String(num)+'元/月';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);		
		}
		public function dianPuYingLi(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num==2000)
				score=50;
			if(num>2000)
			{
				score=50+Math.round((num-2000)/60);
				if(score>100)
					score=100;
			}
			if(num<2000)
			{
				score=50-Math.round((2000-num)/60);
				if(score<0)
					score=0;
			}
			retail.score=score;
			
			var value:String=String(num)+'元/月';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);		
			
		}
		
		public function kuCunGuanLiNengLi(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num==0)
				return;
			
			if(num<7)
				score=60;
			if(num>=7 && num<=14)
				score=70;
			if(num>14)
			{
				var count:Number=(num-14)/7;
				count=Math.round(count)			
				score=70-10*count;
				if(score<0)
					score=0;
			}
			retail.score=score;
			
			var value:String=String(num)+'天';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			retail.id_bar.setProgress(score,100);
		}
		public function jingYingZheShuLinag(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num==0)
				return;
			if(num==1)
				score=50;
			if(num==2)
				score=60;
			if(num>2)
				score=50;
			retail.score=score;
			retail.value=String(num)+'人';
			
			BigPublic.in_retail(retail);
			retail.id_bar.setProgress(score,100);
		}
		public function yingYeShiChang(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num==0)
				return;
			if(num>24)
				num=24;
			if(num<=4 )
				score=num*5;
			if(num>4)
			{
				score=(num-4)*5;
				if(score>100)
					score=100;
			}
			
			retail.score=score;
			
			var value:String=String(num)+'小时';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);
		}
		public function jingYingMianJi(event:Event):void
		{
			var retail:ComplexRetail= event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num==0)
				return;
			if(num<10 )
				score=30;
			if(num>=10 && num<=15)
				score=60;
			if(num>15)
				score=80;
			retail.score=score;
			
			var value:String=String(num)+'平方米';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			retail.id_bar.setProgress(score,100);
		}
	}
}