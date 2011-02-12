package bigzhu_old
{
	import flash.utils.Dictionary;
	
	import mx.containers.Accordion;
	
	public class BigClass implements IBigNote
	{
		public static var crm:CRM;
		public static var notes:Dictionary = new Dictionary();
		public static var reg:RegExp = /big_do_\w+/;
		
		public var calls:Dictionary = new Dictionary();
		public static var all_object:Dictionary = new Dictionary();
		
		public function BigClass()
		{		
			subscribe(this);
		}
		public function subscribe(value:Object):void
		{
			var function_names:Array;
			var function_name:String;
			
			function_names=BigPublic.get_function_name(this);
			
			for(var i:String in function_names)
			{
				
				function_name=function_names[i];
				if(reg.test(function_name))
				{
					if(all_object[function_name] == null)
					{
						var arr:Array=new Array();
						arr.push(value);
						all_object[function_name]=arr;
					}
					else
						(all_object[function_name] as Array).push(value);
					
				}
			}			
			//			if(all_object[value] == null)
			//				all_object[value]=value;
		}
		
		//		public function unsubscribe(value:Object):void
		//		{
		//			if(all_object[value] != null)
		//			{
		//				delete all_object[value];
		//			}
		//		}
		public function getUpperFun():String
		{
			var str:String=(new Error()).getStackTrace().split("at ")[2].split("[")[0].split("/")[1];
			str = str.replace("()", "");
			return str;
		}
		public function getNote():String
		{
			var str:String=(new Error()).getStackTrace().split("at ")[2].split("[")[0].split("/")[1];
			str = str.replace("()", "");
			str = str.replace("big_do_", "");
			return str;
		}
		
		public function send_note(note:String, data:Object=null):void
		{
			var function_name:String='big_do_'+note;
			if(all_object[function_name] ==null)
				return
			else
			{
				var arr:Array = all_object[function_name] as  Array;
				for(var i:String in arr)
				{
					arr[i][function_name](data);
				}
			}	
		}
		public static function send_note(note:String, data:Object=null):void
		{
			var function_name:String='big_do_'+note;
			if(all_object[function_name] ==null)
				return
			else
			{
				var arr:Array=all_object[function_name] as  Array;
				for(var i:String in arr)
				{
					arr[i][function_name](data);
				}
			}	
		}
//		public static function send_note(note:String, data:Object=null):void
//		{
//			for (var item:* in all_object)
//			{
//				var function_names:Array;
//				var function_name:String;
//				function_names=BigPublic.get_function_name(item);
//				
//				for(var i:String in function_names)
//				{
//					function_name=function_names[i];
//					if(function_name=='big_do_'+note)
//					{
//						//						if(data!=null)
//						item[function_name](data);
//						//						else
//						//							item[function_name]();
//					}
//				}
//			}		
//		}
		
		public static const login:String = "login";
		public static const get_privilege:String = "get_privilege";
		public static const login_out:String = "login_out";
		
		
		public static const modify_role:String = "modify_role";
		public static const show_error:String = "show_error";
		public static const get_role_privilege:String = "get_role_privilege";
		public static const delete_role:String = "delete_role";
		
		public static const get_role:String = "get_role";
		public static const get_role_id:String = "get_role_id";
		
		public static const add_role:String = "add_role";
		public static const get_org:String = "get_org";
		public static const get_role_not_privilege:String = "get_role_not_privilege";
		public static const add_role_privilege:String = "add_role_privilege";
		public static const remove_role_privilege:String = "remove_role_privilege";
		
		public static const add_org:String = "add_org";
		public static const del_org:String = "del_org";
		public static const get_org_id:String = "get_org_id";
		public static const change_retail:String = "change_retail";
		public static const get_retail_info:String = "get_retail_info";
		public static const query_report:String = "query_report";
	}
}