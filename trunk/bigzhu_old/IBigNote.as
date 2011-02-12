package bigzhu_old
{
	import flash.utils.Dictionary;

	public interface IBigNote
	{
		/**
		 *订阅 
		 * @param value
		 * 
		 */
		 function subscribe(value:Object):void;
		/**
		 *退订 
		 * @param value
		 * 
		 */
//		function unsubscribe(value:Object):void;
		
		/**
		 *告诉所有订阅的人消息 
		 * 
		 */
		function send_note(note:String, data:Object=null):void;
		
	}
}