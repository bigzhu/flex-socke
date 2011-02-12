package bigzhu
{
	import mx.controls.Image;
	public class StatusBig extends BaseBig
	{
		
		[Embed(source="//icon/status/error.png")]
		public static var error:Class;
		
		[Embed(source="//icon/status/info.png")]
		public static var ok:Class;
		
				public function StatusBig(obj:Object=null)
		{
			super(obj);
		}
		
		public function get comp():Image
		{
			return my_obj as Image;
		}
		
		public function big_do_status_change(obj:Object):void
		{
			if(obj.status == 'error')
				comp.source = error;
			if(obj.status == 'ok')
				comp.source = ok;
			if(obj.show_tip != null)
			{
				obj.show_tip.comp = comp;
				send_note(SHOW_TIP, obj.show_tip)
			}
			
			
		}
	}
}
