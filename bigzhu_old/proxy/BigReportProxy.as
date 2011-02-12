package bigzhu_old.proxy
{
	import bigzhu_old.BigClass;
	
	public class BigReportProxy extends BigClass
	{
		public function BigReportProxy()
		{
			super();
		}
		public function big_do_query_report(obj:Object):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=query_report;
			
			p.gateway.call("retail.queryReport", p.res, obj);
		}
	}
}