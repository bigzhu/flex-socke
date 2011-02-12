package bigzhu_old.proxy
{
	import bigzhu_old.BigClass;
	
	public class BigRetailProxy extends BigClass
	{
		public function BigRetailProxy()
		{
			super();
		}
		public function big_do_change_retail(obj:Object):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=change_retail;
			p.gateway.call("retail.changeRetail", p.res, obj);
		}
		public function big_do_get_retail_info(obj:Object):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=get_retail_info;
			p.gateway.call("retail.getRetailInfo", p.res, obj);
		}
	}
}