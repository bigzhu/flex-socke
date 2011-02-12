/**
 *其他Proxy类的父类,定义了一些调用后台的必要的东西 
 */
package bigzhu_old.proxy
{
	
	import bigzhu_old.BigClass;
	import bigzhu_old.BigTips;
	
	import flash.events.NetStatusEvent;
	import flash.events.SecurityErrorEvent;
	import flash.net.NetConnection;
	import flash.net.Responder;
	import flash.utils.Dictionary;
	
	
	public class BigProxy extends BigClass
	{
		//amf
		public var gateway:NetConnection;
		public var res:Responder; 
		public var result:String;
		public var error_info:String;
		public var do_right_function_name:String;
		public var note_name:String;
		
		//用于存放函数
		public var tips:Dictionary = new Dictionary();
		
		
		public function BigProxy() 
		{
			super();
			
			gateway=new NetConnection();
			gateway.addEventListener(NetStatusEvent.NET_STATUS, onStatus);
			gateway.addEventListener(SecurityErrorEvent.SECURITY_ERROR, onError);
			//						gateway.connect( "http://135.32.9.213:8001");
//			gateway.connect( "http://localhost:8001");
									gateway.connect( "http://10.141.162.118:8001");
			//			gateway.connect( "http://10.104.0.240:8000");
			//			gateway.connect( "http://135.32.89.104:8001");
			//						gateway.connect( "http://116.53.195.181:8001");
			
			//			gateway.connect( "http://116.53.217.72:8001");
			
			res=new Responder(onRight, onError);
		}
		//		public function call(server:String, ...parameters):void
		//		{
		//			gateway.call(server, res, ...parameters);
		//		}
		
		public function onRight(event:*):void
		{
			BigTips.closeTip('connect_fail');
			send_note(note_name+'_over', event.result);
			doRight(event)
		}
		public function doRight(event:*):void
		{
			//			if(do_right_function_name!='')
			//			{
			//				this[do_right_function_name](event);
			//				do_right_function_name='';
			//			}
		}
		/**
		 * amf调用失败
		 * @param event
		 * 
		 */
		public function onError(event:*): void
		{
			error_info='';
			if ( event.hasOwnProperty('description') ) 
			{
				error_info += event.description;
			} 
			else
			{
				error_info  += event;
			}
			send_note('show_error',error_info);
			doError();
		}
		
		/**
		 *出错时候要做的一些动作，用来重载的 
		 * 
		 */
		public function doError():void
		{
		}
		
		public function onStatus( event:NetStatusEvent ): void
		{
			
			error_info = event.info.description;
			
			BigTips.showTip("后台连接不成功,可能是网络异常或者服务在更新,请重新操作: "+error_info, crm ,'connect_fail');
			doError();
		}			
	}
}
