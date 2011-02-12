package bigzhu
{
	import flash.utils.Dictionary;
	
	import mx.events.FlexEvent;
	
	import spark.components.Application;
	
	public class Bigzhu extends Application
	{
		public var comp_map:Dictionary = new Dictionary();
		
		public var tips_big:TipsBig;
		public var login_big:LoginBig;
		public var socket_big:SocketBig;
		
		
		public function Bigzhu()
		{
			super();
			this.addEventListener(FlexEvent.APPLICATION_COMPLETE, initApp);	
			BaseBig.bigzhu_ = this;
		}
		public function initApp(event:FlexEvent):void
		{
			tips_big = new TipsBig();
			login_big = new  LoginBig(comp.id_login_big);
			socket_big = new SocketBig();
			new StatusBig(comp.id_connet_status_image);
		}
		
		public function get comp():Index
		{
			return BaseBig.bigzhu_ as Index;
		}
	}
}