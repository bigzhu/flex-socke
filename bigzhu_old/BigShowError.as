package bigzhu_old
{
	import mx.controls.Alert;
	public class BigShowError extends BigClass
	{
		public function BigShowError()
		{
			super();
		}
		public function big_do_show_error(obj:Object):void
		{
			var error_info:String=String(obj);
			Alert.show(error_info);
		}
	}
}