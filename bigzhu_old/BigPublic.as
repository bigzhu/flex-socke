package bigzhu_old
{
	import flash.events.Event;
	import flash.text.StaticText;
	import flash.utils.describeType;
	import big_component.*;
	
	import mx.controls.Alert;
	import mx.controls.ProgressBar;
	import mx.controls.Tree;
	import mx.formatters.DateFormatter;
	
	import spark.components.DropDownList;
	
	public class BigPublic extends BigClass
	{
				//图标
		[Embed(source="/images/head.png")]
		public static var account_manager_icon:Class;
		
		[Embed(source="/images/retail.png")]
		public static var retail_icon:Class;
		
		[Embed(source="/images/org.png")]
		public static var org_icon:Class;
		
		public function BigPublic()
		{
			
		}
		/**
		 *控制什么作为权限树图标显示 
		 * @param item
		 * @return 
		 * 
		 */
		public static function iconFun(item:Object):*
		{
			if(item.@type=='account_manager')
				return account_manager_icon;
			if(item.@type=='retail')
				return retail_icon;
			if(item.@type=='org')
				return org_icon;	
		}
		/**
		 *控制什么作为权限树名称显示 
		 * @param item
		 * @return 
		 * 
		 */
		public static function treeLabel( item:Object ):String
		{
			if(item.@type=='account_manager')
			{
				return item.@name+'('+item.@id+')';
			}
			else
				return item.@name;
		}
		public  static function setListBar(obj:Object):void
		{
			var list:DropDownList = obj.id_list;
			var bar:ProgressBar=obj.id_bar;
			
			var score:Number= list.selectedItem.score;
			
			bar.setProgress(score,100);
			var value:String=list.selectedItem.label;
			bar.label=value+'('+score+"分)";				
		}
		public  static function setGoodBar(event:Event):void
		{
			var retail:ComplexRetail=event.currentTarget as ComplexRetail;
			var num:Number=retail.id_num.value;
			retail.num=num;
			
			var score:Number=num;
			retail.score=score;
			
			var value:String;
			if(score<=20)
				value='差';
			if(score>20 && score<=40)
				value='较差';
			if(score>40 && score<=60)
				value='中';
			if(score>60 && score<=80)
				value='较好';
			if(score>80 && score<=100)
				value='好';
			retail.value=value;
			in_retail(retail);
			retail.id_bar.setProgress(score,100);
		}
		public static function in_retail(obj:Object):void
		{
			//''' id , flex_id, name, score, value'''
			
			var retail:Object=new Object();
			//id
			retail.id=crm.id_main_view.id_retail.retail_id;
			//flex_id
			retail.flex_id=obj.id;
			//name
			if((obj.parent).hasOwnProperty('label'))
				retail.name=(obj.parent).label;
			else if((obj.parent).hasOwnProperty('title'))
				retail.name=(obj.parent).title;
			else
				retail.name='';
			//score
			retail.score=obj.score;
			//num
			retail.num=obj.num;
			//value
			retail.value=obj.value;
			send_note(change_retail, retail);
		}
		/**
		 *展开树 
		 * @param tree
		 * 
		 */
		public static function expandTree(tree:Tree):void
		{
			tree.validateNow();
			for each(var item:Object in tree.dataProvider)
			tree.expandChildrenOf(item, true);
		}
		
		/**
		 *取得所有函数名 
		 * @param object
		 * @return 
		 * 
		 */
		public static function get_function_name(object:Object):Array
		{
			var function_names:Array=new Array();
			var function_name:String=new String();
			
			var xml:XMLList=describeType(object).method;
			
			for each(var i:XML in xml)
			{
				function_name=i.@name;
				function_names.push(function_name);
			}
			
			return function_names;
			
		}
		
		public static function getChinaTimeDate(date:Date):String
		{                    
			var strChinaTime:String = "";
			var chinaDateFormat:DateFormatter = new DateFormatter();
			var pattern:String = "YYYY年MM月DD日";
			chinaDateFormat.formatString=pattern;
			var formatedDate:String = chinaDateFormat.format(date);                
			var weekPattern:String= "EEE";
			chinaDateFormat.formatString=weekPattern;
			var formatedWeek:String = chinaDateFormat.format(date);   
			strChinaTime = formatedDate;            
			switch ( formatedWeek)
			{                
				case "一":
					formatedWeek = "星期一";
					break;
				case "二":
					formatedWeek = "星期二";
					break;
				case "三":
					formatedWeek = "星期三";
					break;
				case "四":
					formatedWeek = "星期四";
					break;
				case "五":
					formatedWeek = "星期五";
					break;
				case "六":
					formatedWeek = "星期六";
					break;
				case "日":
					formatedWeek = "星期日";
					break;
			}   
			
			strChinaTime += " " + formatedWeek;                    
			return strChinaTime;
		} 
		
	}
}