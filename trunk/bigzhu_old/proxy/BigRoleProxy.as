package bigzhu_old.proxy
{
	import big_component.AddRoleView;
	
	import bigzhu_old.BigClass;
	import bigzhu_old.BigMain;

	
	public class BigRoleProxy extends BigClass
	{
		public var role:Array;
		public var role_privilege:Array;
		public var role_not_privilege:Array;
		public var i_AddRoleView:AddRoleView;

		public function BigRoleProxy()
		{
			super();
		}
		public function big_do_remove_role_privilege(obj:*):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=remove_role_privilege;

			p.gateway.call("server.delRolePrivilege", p.res, obj);
		}
		/**
		 *增加角色权限 
		 * @param obj
		 * 
		 */
		public function big_do_add_role_privilege(obj:*):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=add_role_privilege;
			
			p.gateway.call("server.addRolePrivilege", p.res, obj);
		}
		/**
		 *取得角色已有权限 
		 * @param role_id
		 * 
		 */
		public function big_do_get_role_privilege(role_id:String):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=get_role_privilege;
			
			var select_colum:Array =  ['p.privilege_name','p.privilege_id','p.privilege_type']
			var str:String = new String();
			str = " from privilege p ,role_privilege rp where rp.role_id=";
			str += role_id;
			str += " and p.privilege_id=rp.privilege_id  and p.privilege_id!=1 order by  p.order_id";
			
			p.gateway.call("server.select",p.res,select_colum, str);
		}
		/**
		 *获取角色没有的权限 
		 * @param role_id
		 * 
		 */
		public function big_do_get_role_not_privilege(role_id:String):void
		{	
			var p:BigProxy=new BigProxy();
			p.note_name=get_role_not_privilege;
			
			var select_colum:Array = ['p.privilege_name','p.privilege_id','p.privilege_type']
			var str:String = new String();
			str = " from privilege p where  p.privilege_id not in (select privilege_id from role_privilege  where role_id=";
			str += role_id;
			str += " ) and p.privilege_id!=1  order by  p.order_id";
			
			p.gateway.call("server.select", p.res, select_colum, str);
		}
		
		/**
		 *修改角色 
		 * @param obj
		 * 
		 */
		public function big_do_modify_role(obj:Object):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=modify_role;
			
			p.gateway.call("server.modifyRole", p.res, obj);
		}

		/**
		 *删除角色 
		 * @param role_id
		 * 
		 */
		public function big_do_delete_role(role_id:String):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=delete_role;
			
			var obj:Object=new Object();
			obj.role_id=role_id;
			obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_info[0].staff_id;
			
			p.gateway.call("server.delRole", p.res, obj);
		}
		/**
		 *取得角色信息 
		 * @param staff_id
		 * 
		 */
		public function big_do_get_role(staff_id:String):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=get_role;
			
			var select_colum:Array =  ['role_id', 'name', 'role_desc']
			var str:String = new String();
			str = " from role  where role_id in (select role_id from staff_role where staff_id=";
			str+=staff_id;
			str+=' union all ';
			str+='select role_id from role_log where oper_staff_id=';
			str += staff_id;
			str += " )";
			p.gateway.call("server.select", p.res, select_colum,str);
		}
		/**
		 *取得角色序列 
		 * @param obj
		 * 
		 */
		public function big_do_get_role_id(obj:Object):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=get_role_id;
			
			var select_colum:Array = ['role_seq.nextval role_seq_next']
			var sql:String = "from dual ";
			p.gateway.call("server.select", p.res,select_colum,sql);
			
			i_AddRoleView=obj as AddRoleView;
		}
		/**
		 *增加角色 
		 * @param obj
		 * 
		 */
		public function big_do_add_role(obj:Object):void
		{
			var p:BigProxy=new BigProxy();
			p.note_name=add_role;
			
			p.gateway.call("server.addRole", p.res, obj);
		}
	}
}