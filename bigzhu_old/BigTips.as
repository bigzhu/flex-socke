package bigzhu_old
{
	import flash.geom.Point;
	import flash.utils.Dictionary;
	
	import mx.controls.ToolTip;
	import mx.managers.ToolTipManager;
	public class BigTips
	{
		public function BigTips()
		{
		}
		//用于存放tip
		public static var tips:Dictionary = new Dictionary();
		
		/**
		 *显示tip 
		 * @param content
		 * @param target
		 * @param tip_name
		 * @param x 默认使用target的位置靠右
		 * @param y 默认使用target的位置靠右
		 * @param TipBorderStyle 默认为errorTipRight
		 * 
		 */
		public static function showTip(content:String, target:Object, tip_name:String,
									   
									   x:Number=-1, y:Number=-1, TipBorderStyle:String='errorTipRight'):void
		{
			if(tips[tip_name] == null)
			{
				if(x==-1 && y==-1)
				{
					var pt:Point = new Point(target.x, target.y);
					pt = target.contentToGlobal(pt);
					tips[tip_name] = ToolTipManager.createToolTip(content, pt.x+target.width/2 , pt.y, TipBorderStyle) as ToolTip;
				}
				else
					tips[tip_name] = ToolTipManager.createToolTip(content, x , y, TipBorderStyle) as ToolTip;
				
			}
		}
		
		public static function closeTip(tip_name:String):void
		{	
			if(tips[tip_name] != null)
			{
				ToolTipManager.destroyToolTip(tips[tip_name]);
				delete tips[tip_name];
			}
		}
		public static function clean():void
		{
			for (var key:Object in tips) 
			{ 
				ToolTipManager.destroyToolTip(tips[key]);
				delete tips[key];
			} 
		}
		public static function len():uint
		{
			var len:uint = 0;
			for (var item:* in tips)
				if (item != "mx_internal_uid")
					len++;
			return len;
		}
	}
}
