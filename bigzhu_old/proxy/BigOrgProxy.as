package bigzhu_old.proxy
{
	import bigzhu_old.BigClass;
	public class BigOrgProxy extends BigClass
	{
		public var org:XML;
		public function BigOrgProxy()
		{
			super();
		}
		public function big_do_get_org_id(obj:*):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=get_org_id;
			
			p.gateway.call("retail.getOrgID", p.res);
		}
		public function big_do_get_org(obj:Object):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=get_org;
			
			p.gateway.call("retail.getOrg", p.res, obj);
		}
		public function big_do_get_org_over(obj:*):void 
		{
			org=obj as XML;
		}
		public function big_do_del_org(obj:*):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=del_org;
			p.gateway.call("retail.delOrg", p.res, obj);
		}
		public function big_do_add_org(obj:*):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=add_org;
			
			p.gateway.call("retail.addOrg", p.res, obj);
		}
	}
}