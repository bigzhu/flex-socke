package core
{
	
	/**
	 * ...主题的接口
	 * @author spadeA
	 */
	public interface ISubject
	{
		function registerObServer(value:IObServer):void;
		function removeObServer(value:IObServer):void;
		function notifyObServer():void;
	}
	
}

package core
{
	
	/**
	 * ...观察者的接口
	 * @author spadeA
	 */
	public interface IObServer
	{
		function update(value:String):void;
	}
	
}

package 
{
	import core.IObServer;
	import core.ISubject;
	
	/**
	 * ...报社
	 * @author spadeA
	 */
	public class NewsPaperOffice implements ISubject
	{
		private var obServerList:Array;
		private var newsPaperType:String;
		public function NewsPaperOffice()
		{
			obServerList = new Array();
		}
		
		public function registerObServer(value:IObServer):void {
			obServerList.push(value);
		}
		
		public function removeObServer(value:IObServer):void {
			var index:int = obServerList.indexOf(value);
			if (index>0) 
			{
				obServerList.splice(index, 1);
			}
		}
		
		public function notifyObServer():void {
			for (var i:int = 0; i < obServerList.length; i++ ) 
			{
				obServerList[i].update(newsPaperType);
			}
		}
		
		public function publishNewsPaper(value:String):void {
			newsPaperType = value;
			notifyObServer();
		}
	}
	
}

package 
{
	import core.IObServer;
	import core.ISubject;
	
	/**
	 * ...张三
	 * @author spadeA
	 */
	public class ObserverOne implements IObServer
	{
		private var newsPaperOffice:ISubject
		public function ObserverOne(value:ISubject)
		{
			newsPaperOffice = value;
			newsPaperOffice.registerObServer(this);
		}
		
		public function update(value:String):void {
			trace("恩，服务貌似不错！我订阅的:"+value+"收到了");
		}		
	}
	
}

package 
{
	import core.IObServer;
	import core.ISubject;
	
	/**
	 * ...李四
	 * @author spadeA
	 */
	public class ObserverTwo implements IObServer
	{
		private var newsPaperOffice:ISubject
		public function ObserverTwo(value:ISubject)
		{
			newsPaperOffice = value;
			newsPaperOffice.registerObServer(this);
		}
		
		public function update(value:String):void {
			trace("哈哈,订阅的报纸来啦!"+value);
		}
		
	}
	
}

//////////////////////////////////////华丽的分割线////////////////////////////////////////////////

package
{
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author spadeA
	 */
	public class Main extends Sprite
	{
		private var _office:NewsPaperOffice;
		public function Main():void
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
			initApp();
		}
		
		private function initApp():void {
			_office = new NewsPaperOffice();
			
			var obOne:ObserverOne = new ObserverOne(_office);
			var obTwo:ObserverTwo = new ObserverTwo(_office);
			
			_office.publishNewsPaper("新华日报");
		}
		
	}
	
}