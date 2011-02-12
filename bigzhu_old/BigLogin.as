package bigzhu_old
{
	import bigzhu_old.BigTips;
	import bigzhu_old.proxy.*;
	
	import flash.events.MouseEvent;
	
	import mx.controls.Alert;
	
	public class BigLogin extends BigClass
	{
		public function BigLogin()
		{
			super();
			crm.id_login.id_login_button.addEventListener(MouseEvent.CLICK, doLogin);
			crm.id_login_out.addEventListener(MouseEvent.CLICK, loginOut);
		}
		public function loginOut(event:MouseEvent):void
		{
			send_note(login_out);
		}
		public function doLogin(event:MouseEvent):void
		{
			var obj:Object=new Object();
			obj.staff_id=crm.id_login.id_staff_id.text;
			obj.passwd=crm.id_login.id_passwd.text;
			
			if(obj.staff_id=="")
			{
				BigTips.showTip("请输入工号！", crm.id_login.id_staff_id , "staff_id_is_null");
				return;
			}
			else
				BigTips.closeTip("staff_id_is_null");
			
			if(obj.passwd=="")
			{
				BigTips.showTip("请输入密码！", crm.id_login.id_passwd , "passwd_is_null");
				return;
			}
			else
				BigTips.closeTip("passwd_is_null");
			
			send_note(login, obj)
		}
		
		public function big_do_login_over(obj:Object):void
		{
			send_note(get_privilege, obj[0].staff_id);
			
			crm.id_top_stack.selectedChild=crm.id_nav_main;

			var d:Date = new Date();
			crm.id_welcome.text=obj[0].staff_desc+
				"("+obj[0].staff_id+")"
				+"，目前登录系统版本 "+" "+"今天是"+BigPublic.getChinaTimeDate(d)+"!";
		}
		public function big_do_login_out(obj:*):void
		{
			crm.id_top_stack.selectedChild=crm.id_nav_login;
		}
		
	}
}
