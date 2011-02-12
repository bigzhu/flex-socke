package bigzhu_old
{
	import big_component.Business;
	import big_component.ComplexRetail;
	
	import flash.events.Event;
	import flash.events.FocusEvent;
	import flash.utils.Dictionary;
	
	import mx.collections.ArrayCollection;
	
	import spark.events.IndexChangeEvent;
	
	public class BigBusiness extends BigClass
	{
		public var elements:Dictionary = new Dictionary();
		
		public var business:Business ;
		
		public function BigBusiness()
		{
			super();
			business=crm.id_main_view.id_retail.id_bussion;
			init_data();
			add_all();
			//禁用
			able_all(false);
			add_event();
			show_what();
		}
		
		public function show_num_text(retail:ComplexRetail):void
		{
			rm_text_input(retail);
			//			rm_num(retail);
			rm_bar(retail);
			rm_list(retail);
			//			rm_text(retail);
			
		}
		public function show_list_bar_text(retail:ComplexRetail):void
		{
			rm_text_input(retail);
			rm_num(retail);
			//rm_bar(retail);
			//rm_list(retail);
			//			rm_text(retail);
			
		}
		public function show_text_input(retail:ComplexRetail):void
		{
			//rm_text_input(retail);
			rm_num(retail);
			rm_bar(retail);
			rm_list(retail);
			rm_text(retail);
		}
		public function show_list(retail:ComplexRetail):void
		{
			rm_text_input(retail);
			rm_num(retail);
			rm_bar(retail);
			//rm_list(retail);
			rm_text(retail);
		}
		public function show_num_bar_text(retail:ComplexRetail):void
		{
			rm_text_input(retail);
			//			rm_num(retail);
			//			rm_bar(retail);
			rm_list(retail);
			//rm_text(retail);
		}
		public function show_text_input_list(retail:ComplexRetail):void
		{
			//				rm_text_input(retail);
			rm_num(retail);
			rm_bar(retail);
			//			rm_list(retail);
			rm_text(retail);
		}
		public function rm_text(retail:ComplexRetail):void
		{
			retail.removeElement(retail.id_text);
		}
		public function rm_list(obj:*):void
		{
			obj.removeElement(obj.id_list);
		}
		public function rm_text_input(obj:*):void
		{
			obj.removeElement(obj.id_text_input);
		}
		public function rm_bar(obj:*):void
		{
			obj.removeElement(obj.id_bar);
		}
		public function rm_num(obj:*):void
		{
			obj.removeElement(obj.id_num);
		}
		public function add_detail_data(obj:*):void
		{
			
			for each (var retail:ComplexRetail in elements)
			{
				retail.num=-1;
				retail.score=-1;
				retail.value='未设定';
				if(retail.hasOwnProperty('id_bar'))
				{
					retail.id_bar.setProgress(0,100);
				}
				
			}
			for each (var item:Object in obj)
			{ 
				if(elements.hasOwnProperty(item.flex_id))
				{
					//					if(elements[item.flex_id].hasOwnProperty('score'))
					elements[item.flex_id].score= Number(item.score);
					//					if(elements[item.flex_id].hasOwnProperty('num'))
					elements[item.flex_id].num= Number(item.num);
					//					if(elements[item.flex_id].hasOwnProperty('value'))
					elements[item.flex_id].value= item.value;
					//					if(elements[item.flex_id].hasOwnProperty('id_bar'))
					//显示进度
					elements[item.flex_id].id_bar.setProgress(elements[item.flex_id].score, 100)
					//droplist 显示 prompt
					elements[item.flex_id].id_list.selectedIndex=-1;
				}
			}
		}
		/**
		 *加入需要操作的组件到字典中 
		 * 
		 */
		public function add_all():void
		{
			//所有元素	
			add_to(business.id_diLiHuanJing);
			add_to(business.id_shouFaHuanJing);
			add_to(business.id_touZiHuanJing);
			add_to(business.id_jingJiFaZhanYuQi);
			add_to(business.id_kaiFangChenDu);
			add_to(business.id_shaoShuMingZuWenHua);
			add_to(business.id_teShuFengShuXiGuan);
			add_to(business.id_zhuYaoJingJiZhiZhu);
			add_to(business.id_xiaoFeiPianHao);
			add_to(business.id_zhongDianxiaoShouJiJie);
			add_to(business.id_xiaoFeiNengLi);
			add_to(business.id_xiaoFeiYiShi);
			add_to(business.id_xiaoFeiZheShuLiang);
			add_to(business.id_guDingXiaoFeiZheShuLiang);
			add_to(business.id_nianLingGouChen);
			add_to(business.id_shanQuanXiaoFeiShuLiang);
			add_to(business.id_shanQuanXiaoFeiJieGou);
			add_to(business.id_xiaoFeiZheZhiYeGouChen);
			add_to(business.id_dianPuQuYu);
			add_to(business.id_nianLingGouChen);
			add_to(business.id_xiaoFeiZheZhiYeGouChen);
			add_to(business.id_xiaoFeiDongJi);
			add_to(business.id_pinXiPiaoHao);
			add_to(business.id_pinPaiPianHao);
			add_to(business.id_shouRuShuiPing);
			add_to(business.id_xuanChuangQuDao);
			add_to(business.id_TiShenJieGou);
			add_to(business.id_gouMaiDiDian);
			add_to(business.id_gouMaiDiYingXiangYinSu);
		}
		public function show_what():void
		{
			var retail:ComplexRetail;
			
			retail=business.id_diLiHuanJing;
			show_list(retail);
			
			retail=business.id_shouFaHuanJing;
			show_num_bar_text(retail);
			
			retail=business.id_touZiHuanJing;
			show_num_bar_text(retail);
			
			retail=business.id_jingJiFaZhanYuQi;
			show_num_bar_text(retail);
			
			retail=business.id_xiaoFeiYiShi;
			show_num_bar_text(retail);
			
			retail=business.id_kaiFangChenDu;
			show_num_bar_text(retail);
			
			retail=business.id_shaoShuMingZuWenHua;
			show_text_input(retail);
			
			retail=business.id_teShuFengShuXiGuan;
			show_text_input(retail);
			
			retail=business.id_zhuYaoJingJiZhiZhu;
			show_text_input(retail);
			
			retail=business.id_xiaoFeiPianHao;
			show_text_input(retail);
			
			retail=business.id_zhongDianxiaoShouJiJie;
			show_text_input(retail);
			
			retail=business.id_xiaoFeiNengLi;
			show_list_bar_text(retail);
			
			retail=business.id_dianPuQuYu;
			show_list_bar_text(retail);
			
			retail=business.id_nianLingGouChen;
			show_num_bar_text(retail);
			
			retail=business.id_xiaoFeiZheZhiYeGouChen;
			show_text_input(retail);
			
			retail=business.id_guDingXiaoFeiZheShuLiang;
			show_num_bar_text(retail);
			
			retail=business.id_shanQuanXiaoFeiShuLiang;
			show_num_bar_text(retail);
			
			retail=business.id_shanQuanXiaoFeiJieGou;
			show_num_bar_text(retail);
			
			retail=business.id_xiaoFeiZheShuLiang;
			show_num_bar_text(retail);
			
			retail=business.id_xuanChuangQuDao;
			show_text_input_list(retail);
			
			retail=business.id_xiaoFeiDongJi;
			show_text_input_list(retail);
			
			retail=business.id_pinXiPiaoHao;
			show_text_input_list(retail);
			
			retail=business.id_pinPaiPianHao;
			show_text_input_list(retail);
			
			retail=business.id_shouRuShuiPing;
			show_num_bar_text(retail);
			
			retail=business.id_TiShenJieGou;
			show_text_input_list(retail);
			
			retail=business.id_gouMaiDiDian;
			show_text_input_list(retail);
			retail=business.id_gouMaiDiYingXiangYinSu;
			show_text_input_list(retail);
		}
		/**
		 *加入事件处理 
		 * 
		 */
		public function add_event():void
		{
			//事件
			business.id_teShuFengShuXiGuan.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			business.id_shaoShuMingZuWenHua.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			business.id_zhuYaoJingJiZhiZhu.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			business.id_xiaoFeiPianHao.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			business.id_zhongDianxiaoShouJiJie.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			business.id_xiaoFeiZheZhiYeGouChen.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input);
			
			business.id_xiaoFeiNengLi.addEventListener(FocusEvent.FOCUS_OUT, just_in_list);
			business.id_dianPuQuYu.addEventListener(FocusEvent.FOCUS_OUT, just_in_list);
			
			business.id_diLiHuanJing.addEventListener(IndexChangeEvent.CHANGE, diLiHuanJing);
			business.id_nianLingGouChen.addEventListener(FocusEvent.FOCUS_OUT, nianLingGouChen);
			
			
			business.id_shouFaHuanJing.addEventListener(FocusEvent.FOCUS_OUT, BigPublic.setGoodBar);
			business.id_touZiHuanJing.addEventListener(FocusEvent.FOCUS_OUT, BigPublic.setGoodBar);
			business.id_jingJiFaZhanYuQi.addEventListener(FocusEvent.FOCUS_OUT, BigPublic.setGoodBar);
			
			business.id_xiaoFeiYiShi.addEventListener(FocusEvent.FOCUS_OUT, xiaoFeiYiShi);
			business.id_kaiFangChenDu.addEventListener(FocusEvent.FOCUS_OUT, kaiFangChenDu);		
			business.id_guDingXiaoFeiZheShuLiang.addEventListener(FocusEvent.FOCUS_OUT, guDingXiaoFeiZheShuLiang);		
			business.id_shanQuanXiaoFeiShuLiang.addEventListener(FocusEvent.FOCUS_OUT, shanQuanXiaoFeiShuLiang);		
			business.id_shanQuanXiaoFeiJieGou.addEventListener(FocusEvent.FOCUS_OUT, shanQuanXiaoFeiJieGou);		
			business.id_shouRuShuiPing.addEventListener(FocusEvent.FOCUS_OUT, shouRuShuiPing);		
			
			business.id_xuanChuangQuDao.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input_list);		
			business.id_xiaoFeiDongJi. addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input_list);		
			business.id_pinXiPiaoHao.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input_list);		
			business.id_pinPaiPianHao.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input_list);		
			business.id_TiShenJieGou.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input_list);		
			business.id_gouMaiDiDian.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input_list);		
			business.id_gouMaiDiYingXiangYinSu.addEventListener(FocusEvent.FOCUS_OUT, just_in_text_input_list);		
		}
		/**
		 *初始化数据 
		 * 
		 */
		public function init_data():void
		{
			business.id_xiaoFeiNengLi.id_list.dataProvider=new ArrayCollection([
				{label:"一类烟", score:100}, 
				{label:"二类烟", score:80}, 
				{label:"三类烟", score:60}, 
				{label:"四类烟", score:40}, 
				{label:"五类烟", score:20}, 
			]);
			business.id_diLiHuanJing.id_list.dataProvider=new ArrayCollection([
				{label:"城区", score:-1}, 
				{label:"镇区", score:-1}, 
				{label:"城乡结合部", score:-1}, 
				{label:"乡村(坝区)", score:-1}, 
				{label:"乡村(山区)", score:-1}, 
			]);
			
			business.id_dianPuQuYu.id_list.dataProvider=new ArrayCollection([
				{label:"商业正街", score:80}, 
				{label:"集贸市场", score:80}, 
				{label:"娱乐场所A", score:80}, 
				{label:"生活小区A", score:80}, 		
				{label:"工矿区", score:80}, 		
				
				{label:"镇区", score:60}, 		
				{label:"口岸及主要交通干道", score:60}, 		
				
				{label:"娱乐场所B", score:40}, 		
				{label:"生活小区B", score:40}, 		
				{label:"小巷", score:40}, 		
				{label:"村寨", score:40}, 		
			]);
			business.id_xiaoFeiDongJi.id_list.dataProvider=new ArrayCollection([
				{label:"社交需要", score:-1}, 
				{label:"生理需要", score:-1}, 
				{label:"工作需要", score:-1}, 
				{label:"从众影响", score:-1}, 
				{label:"调节情绪", score:-1}, 
				{label:"其它", score:-1}, 
			]);
			business.id_pinXiPiaoHao.id_list.dataProvider=new ArrayCollection([
				{label:"劲头力度", score:-1}, 
				{label:"品吸习惯", score:-1}, 
				{label:"香料配方", score:-1}, 
				{label:"烟叶品质", score:-1}, 
				{label:"焦油含量", score:-1}, 
				{label:"其它", score:-1}, 
			]);
			business.id_pinPaiPianHao .id_list.dataProvider=new ArrayCollection([
				{label:"中华", score:-1}, 
				{label:"云烟", score:-1}, 
				{label:"玉溪", score:-1}, 
				{label:"红塔山", score:-1}, 
				{label:"红河", score:-1}, 
				{label:"七匹狼", score:-1}, 
				{label:"双喜", score:-1}, 
				{label:"红梅", score:-1}, 
				{label:"红山茶", score:-1}, 
				{label:"红旗渠", score:-1}, 
				{label:"其它", score:-1}, 
			]);
			business.id_shouRuShuiPing .id_num.maximum=99999999;
			business.id_xuanChuangQuDao.id_list.dataProvider=new ArrayCollection([
				{label:"媒体宣传", score:-1}, 
				{label:"朋友推荐", score:-1}, 
				{label:"烟草企业促销赞助", score:-1}, 
				{label:"零售户推荐", score:-1}, 
				{label:"自行了解", score:-1}, 
				{label:"其它", score:-1}, 
			]);
			
			business.id_TiShenJieGou .id_list .dataProvider=new ArrayCollection([
				{label:"朋友家人聚会消遣", score:-1}, 
				{label:"逢年过节", score:-1}, 
				{label:"办事送礼", score:-1}, 
				{label:"公务活动", score:-1}, 
				{label:"其它", score:-1}, 
			]);
			business.id_gouMaiDiDian .id_list .dataProvider=new ArrayCollection([
				{label:"固定地点购买", score:-1}, 
				{label:"就近购买", score:-1}, 
				{label:"购买其它用品时顺便购买", score:-1}, 
				{label:"熟人购买", score:-1}, 
				{label:"其它", score:-1}, 
			]);
			
			business.id_gouMaiDiYingXiangYinSu.id_list .dataProvider=new ArrayCollection([
				{label:"店铺位置", score:-1}, 
				{label:"店铺形象", score:-1}, 
				{label:"营业时间", score:-1}, 
				{label:"销售价格", score:-1}, 
				{label:"与经营者关系", score:-1}, 
				{label:"其它", score:-1}, 
			]);
		}
		public function shouRuShuiPing(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num==2000)
				score=40;
			if(num<2000)
			{
				score=40-Math.round((2000-num)/100);
				if(score<20)
					score=20;
			}
			if(num>2000)
			{
				score=40+Math.round((num-200)/100);
				if(score>100)
					score=100;
			}
			retail.score=score;
			
			var value:String=String(num)+'元';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);		
		}
		
		public function shanQuanXiaoFeiJieGou(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num==100)
				score=50;
			if(num<100)
			{
				score=50-Math.round((100-num)/4);
				if(score<0)
					score=0;
			}
			if(num>100)
			{
				score=50+Math.round((num-100)/4);
				if(score>100)
					score=100;
			}
			retail.score=score;
			
			var value:String=String(num)+'元/条';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);
		}
		
		public function just_in_text_input_list(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			retail.num=-1;
			retail.score=-1;
			retail.value=retail.id_list.selectedItem.label;
			retail.value=retail.id_text_input.text;
			
			BigPublic.in_retail(retail);
		}
		
		public function just_in_list(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			retail.num=-1;
			retail.score=retail.id_list.selectedItem.score;
			retail.value=retail.id_list.selectedItem.label;
			
			BigPublic.in_retail(retail);
			retail.id_bar.setProgress(retail.score, 100);
		}
		
		public function just_in_text_input(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			retail.num=-1;
			retail.score=-1;
			retail.value=retail.id_text_input.text;
			BigPublic.in_retail(retail);
		}
		public function diLiHuanJing(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			retail.num=-1;
			retail.score=-1;
			retail.value=retail.id_list.selectedItem.label;
			BigPublic.in_retail(retail);
		}
		/**
		 *让所有组件不可用 
		 * 
		 */
		public function able_all(b:Boolean):void
		{
			for each (var item:Object in elements)
			{ 
				item.enabled=b; 
			}
		}
		
		
		public function add_to(obj:Object):void
		{
			elements[obj.id]=obj;
		}
		public function shanQuanXiaoFeiShuLiang(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number=num;
			if(score>100)
				score=100
			retail.score=score;
			
			
			var value:String;
			if(num<24)
				value='三类区域'+'('+String(num)+'箱/月)';
			if(num>=24 && num<=36)
				value='二类区域'+'('+String(num)+'箱/月)';
			if(num>36)
				value='一类区域'+'('+String(num)+'箱/月)';
			
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);
		}
		public function guDingXiaoFeiZheShuLiang(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			var num:Number=retail.id_num.value;
			retail.num=num;
			var score:Number;
			if(num==80)
				score=50;
			if(num<80)
			{
				score=50-Math.round((80-num)/2);
				if(score<20)
					score=20;
			}
			if(num>80)
			{
				score=50+Math.round((num-80)/2);
				if(score>100)
					score=100;
			}
			retail.score=score;
			
			var value:String=String(num)+'人/月';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);
			
		}
		public function nianLingGouChen(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number;
			if(num<18 )
				score=0;
			if(num>=18 && num<=22)
				score=50;
			if(num>=23 && num<=30)
				score=60;
			if(num>=31 && num<=50)
				score=80;
			if(num>50)
				score=40;
			
			retail.score=score;
			
			var value:String=String(num)+'岁';
			retail.value=value;
			
			BigPublic.in_retail(retail);
			
			retail.id_bar.setProgress(score,100);
		}
		public function kaiFangChenDu(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number=num-5;
			if(score<0)
				score=0;
			retail.score=score;
			business.id_kaiFangChenDu.id_bar.setProgress(score,100);
			var value:String=' ';
			retail.value=value;
			
			BigPublic.in_retail(retail);
		}
		//消费意识
		public function xiaoFeiYiShi(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number=num;
			retail.score=score;
			retail.id_bar.setProgress(score,100);
			
			var value:String;
			if(score<=25)
				value='淡薄';
			if(score>25 && score<=50)
				value='一般';
			if(score>50 && score<=75)
				value='较好';
			if(score>75 && score<=100)
				value='强烈';
			retail.value=value;		
			BigPublic.in_retail(retail);
		}
	}
}