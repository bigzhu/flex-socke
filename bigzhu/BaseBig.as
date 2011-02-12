package bigzhu
{
	import bigzhu.Bigzhu;
	
	import flash.net.Socket;
	import flash.utils.Dictionary;
	
	import mx.controls.Alert;
	
	public class BaseBig
	{
		//action note
		public static const LOGIN:String = 'login';
		public static const STATUS_CHANGE:String = 'status_change';
		//tips note
		public static const CLOSE_TIP:String = 'close_tip';
		public static const SHOW_TIP:String = 'show_tip';
		public static const CLEAN_TIP:String = 'clean_tip';
		
		public static const TIP_ERROR:String = 'tip_error';
		public static const TIP_CONNECT_IS_FAILED:String = 'tip_connect_is_failed';
		public static const TIP_STAFF_ID_IS_NULL:String = 'tip_staff_id_is_null';
		public static const TIP_PASSWD_IS_NULL:String = 'tip_passwd_is_null';
		
		//把主页面实例传给我
		public static var bigzhu_:Bigzhu;
		public static var socket_big:SocketBig;
		public static var all_object:Dictionary = new Dictionary();
		
		public var my_obj:Object;
		
		
		public function BaseBig(obj:Object = null)
		{
			this.my_obj = obj;
			//实例化的时候自动注册
			subscribe(this);
		}
		
		/**
		 *用big_do前缀函数名,注册组件实例 
		 * @param value 实例组建
		 * 
		 */
		public function subscribe(value:Object):void
		{
			var reg:RegExp = /big_do_\w+/;
			
			var function_names:Array = Public.get_function_name(this);
			
			for(var i:String in function_names)
			{
				var function_name:String = function_names[i];
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
		}
		
		/**
		 *发送消息 
		 * @param note
		 * @param data
		 * 
		 */
		public static function send_note(note:String, data:Object=null):void
		{
			var function_name:String='big_do_'+note;
			if(all_object[function_name] ==null)
			{
				Alert.show('未定义对消息'+note+'的处理函数'+function_name);
				return
			}
			else
			{
				var arr:Array=all_object[function_name] as  Array;
				for(var i:String in arr)
				{
					arr[i][function_name](data);
				}
			}	
		}
		
		
	}
}