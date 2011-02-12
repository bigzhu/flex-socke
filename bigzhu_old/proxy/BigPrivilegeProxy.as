package bigzhu_old.proxy
{
	import bigzhu_old.BigClass;
	
	public class BigPrivilegeProxy extends BigClass
	{
		public var privilege:XML;

		public function BigPrivilegeProxy()
		{
			super();
		}
		public function big_do_get_privilege(obj:Object):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=get_privilege;
			
			p.gateway.call("server.getPrivilege", p.res, obj);
		}
		public function big_do_get_privilege_over(event:*):void 
		{
			privilege=event.result as XML;
		}
	}
}