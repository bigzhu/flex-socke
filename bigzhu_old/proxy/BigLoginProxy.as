package bigzhu_old.proxy
{
	import bigzhu_old.BigClass;
	
	public class BigLoginProxy extends BigClass
	{
		public var staff_id:String;
		public var passwd:String;
		public var staff_info:Array = new Array() ;

		public function BigLoginProxy()
		{
			super();
		}
		public function big_do_login(obj:Object):void
		{
			var p:BigProxy=new BigProxy();
//			p.note_name=getNote();
			p.note_name=login;
			staff_id=obj.staff_id;
			p.gateway.call("server.loginStaff", p.res, obj.staff_id, obj.passwd);
		}
		 public function big_do_login_over(obj:Object):void 
		{
			staff_info=obj as Array;
		}
	}
}