package bigzhu
{
	import big_component.Login;
	
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	import org.osmf.layout.AbsoluteLayoutFacet;
	
	public class LoginBig extends BaseBig
	{
		public var staff_info:Array;

		public function LoginBig(obj:Object=null)
		{
			super(obj);
			
			comp.id_login_button.addEventListener(MouseEvent.CLICK, login)
		}
		public function get comp():Login
		{
			return my_obj as Login;
		}
		
		public function login(event:Event):void
		{
			var obj:Object = new Object();
			obj.staff_id = comp.id_staff_id.text;
			obj.passwd = comp.id_passwd.text;
			
			var show_tip:Object = new Object();
			
			show_tip.info = '请输入工号！';
			if(obj.staff_id=="")
			{
				show_tip.comp = comp.id_staff_id;
				send_note(SHOW_TIP, show_tip)
				return;
			}
			else
				send_note(CLOSE_TIP, show_tip.info)
			
			show_tip.info = '请输入密码！';
			if(obj.passwd=="")
			{
				show_tip.comp = comp.id_passwd;
				send_note(SHOW_TIP, show_tip)
				return;
			}
			else
				send_note(CLOSE_TIP, show_tip.info)
			
			send_note(LOGIN, obj)
		}
		
		public function big_do_login(obj:Object):void
		{
			var send_data:Object = new Object();
			send_data.note = 'login';
			send_data.value = obj;
			socket_big.write(send_data);	
		}
		
		public function big_do_login_over(obj:Object):void
		{
			staff_info = obj as Array;
		}
	}
}