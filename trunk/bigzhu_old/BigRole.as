package bigzhu_old
{
	import big_component.*;
	
	import flash.events.ContextMenuEvent;
	import flash.events.MouseEvent;
	import flash.ui.ContextMenu;
	import flash.ui.ContextMenuItem;
	
	import mx.collections.*;
	import mx.controls.Button;
	import mx.controls.DataGrid;
	import mx.events.DataGridEvent;
	import mx.managers.PopUpManager;
	
	import spark.components.*;
	
	public class BigRole extends BigClass	
	{
		//角色记录
		public var role:DataGrid;
		//增加工号页面
		public var add_role_view:AddRoleView;
		//删除员工密码检查页面
		public var del_role_check_passwd_view:CheckPassword;
		//显示权限页面
		public var privilege_view:Privilege;
		//角色id
		public var role_id:String;
		
		public function BigRole()
		{
			super();
			role=crm.id_main_view.id_role.id_role_datagrid;
			addLeft();
			role.addEventListener(DataGridEvent.ITEM_EDIT_END, modifyRole);
			//role.contextMenu=context_menu;
		}
		public function big_do_get_role_over(obj:Object):void
		{
			role.dataProvider=obj;
		}
		/**
		 *修改角色 
		 * @param evnet
		 * 
		 */
		public function modifyRole(event:DataGridEvent):void
		{
			var obj:Object=new Object();
			obj.role_id=event.target.selectedItem.role_id;
			obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_info[0].staff_id;
			
			if(event.dataField=='name')
			{
				if(event.target.selectedItem.name==event.currentTarget.itemEditorInstance.text)
					return;
				obj.name=event.currentTarget.itemEditorInstance.text;
			}
			if(event.dataField=='role_desc')
			{
				if(event.target.selectedItem.role_desc==event.currentTarget.itemEditorInstance.text)
					return;
				obj.role_desc=event.currentTarget.itemEditorInstance.text;
			}
			
			send_note(modify_role, obj);
		}
		/**
		 *增加右键菜单 
		 * 
		 */
		public function addLeft():void
		{
			role.contextMenu=new ContextMenu();	
			
			var add_role:ContextMenuItem = new ContextMenuItem("增加角色");
			add_role.addEventListener(ContextMenuEvent.MENU_ITEM_SELECT, showAddRoleView);
			role.contextMenu.customItems.push(add_role);
			
			var bind_privelge:ContextMenuItem=new ContextMenuItem("给角色指定权限")
			bind_privelge.addEventListener(ContextMenuEvent.MENU_ITEM_SELECT, showPrivelge);
			role.contextMenu.customItems.push(bind_privelge);
			
			var del_role:ContextMenuItem = new ContextMenuItem("删除角色");
			del_role.addEventListener(ContextMenuEvent.MENU_ITEM_SELECT, showdeleteRoleCheckPasswd);
			role.contextMenu.customItems.push(del_role);
			
			//			var xSelectRoleStaff:ContextMenuItem = new ContextMenuItem("查询拥有此角色的工号");
			//			xSelectRoleStaff.addEventListener(ContextMenuEvent.MENU_ITEM_SELECT,selectRoleStaff);
			role.contextMenu.hideBuiltInItems();
		}
		public function showPrivelge(event:ContextMenuEvent):void
		{
			if(!event.mouseTarget.hasOwnProperty('data'))
			{
				send_note(show_error,'请点击需要修改权限的角色！');
				return;
			}

			privilege_view=new Privilege();
			PopUpManager.addPopUp(privilege_view, role, false); 
			PopUpManager.centerPopUp(privilege_view);	
			
			privilege_view.id_add.addEventListener(MouseEvent.CLICK, addPrivilege);
			privilege_view.id_remove.addEventListener(MouseEvent.CLICK, removePrivilege);
			
			role_id=event.mouseTarget['data'].role_id;
			var role_name:String=event.mouseTarget['data'].name;
			privilege_view.title="给角色"+role_name+"("+role_id+")"+"修改权限";
			send_note(get_role_privilege, role_id);
			send_note(get_role_not_privilege, role_id);
		}
		/**
		 *加入权限 
		 * @param event
		 * 
		 */
		public function addPrivilege(event:MouseEvent):void
		{
			var obj:Object=privilege_view.id_not_have_privilege.selectedItem;
			if(obj==null)
			{
				send_note(show_error,'请点击需要增加的权限！');
				return;
			}
			var add_p:Object=new Object();
			add_p.privilege_id=obj.privilege_id;
			add_p.role_id=role_id;
			add_p.oper_staff_id=BigMain.i_BigLoginProxy.staff_id;
			send_note(add_role_privilege, add_p);
		}
		public function big_do_add_role_privilege_over(obj:*):void
		{
			send_note(get_role_privilege, role_id);
			send_note(get_role_not_privilege, role_id);
		}
		public function removePrivilege(event:MouseEvent):void
		{
			var obj:Object=privilege_view.id_has_privilege.selectedItem;
			if(obj==null)
			{
				send_note(show_error,'请点击需要删除的权限！');
				return;
			}
			var remove_p:Object=new Object();
			remove_p.privilege_id=obj.privilege_id;
			remove_p.role_id=role_id;
			remove_p.oper_staff_id=BigMain.i_BigLoginProxy.staff_id;
			send_note(remove_role_privilege, remove_p);
		}
		public function big_do_remove_role_privilege(obj:*):void
		{
			send_note(get_role_privilege, role_id);
			send_note(get_role_not_privilege, role_id);
		}
		public function big_do_get_role_privilege_over(obj:Object):void
		{
			if(obj==null)
				return;
			var arr_has:Array=merage(obj as Array);
			
			privilege_view.id_has_privilege.dataProvider=arr_has;
		}
		public function big_do_get_role_not_privilege_over(obj:Object):void
		{
			if(obj==null)
				return;
			var arr_not:Array=merage(obj as Array);
			
			privilege_view.id_not_have_privilege.dataProvider=arr_not;
		}
		public function merage(arr:Array):Array
		{
			for(var i:int=0;i<arr.length;++i)
			{
				if(arr[i].privilege_type=="classified")
				{
					arr[i].privilege=arr[i].privilege_name+"(分类)";
				}
				else
				{
					arr[i].privilege=arr[i].privilege_name;
				}
			}
			return arr;
		}
		/**
		 *显示删除角色时候的密码验证
		 * @param event
		 * 
		 */
		public function showdeleteRoleCheckPasswd(event:ContextMenuEvent):void
		{
			if(del_role_check_passwd_view==null)
				del_role_check_passwd_view=new CheckPassword();
			PopUpManager.addPopUp(del_role_check_passwd_view, role, false); 
			PopUpManager.centerPopUp(del_role_check_passwd_view);
			
			del_role_check_passwd_view.note_name=delete_role;
			
			if(!event.mouseTarget.hasOwnProperty('data'))
			{
				send_note('show_error','请点击需要删除的角色！');
				return;
			}
			else
			{
				var role_id:String=event.mouseTarget['data'].role_id;
				del_role_check_passwd_view.obj=role_id;
//				send_note(delete_role, role_id);
			}
		}
		public function big_do_delete_role_over(obj:*):void
		{
			send_note(get_role, BigMain.i_BigLoginProxy.staff_info[0].staff_id)		
		}
		/**
		 *显示增角色界面 
		 * @param event
		 * 
		 */
		public function showAddRoleView(event:ContextMenuEvent):void
		{
			if(add_role_view==null)
				add_role_view=new AddRoleView();
			
			PopUpManager.addPopUp(add_role_view, role, false); 
			PopUpManager.centerPopUp(add_role_view);
			send_note(get_role_id, add_role_view);
			(add_role_view.id_add as mx.controls.Button).addEventListener(MouseEvent.CLICK, addRole);	
		}
		public function big_do_get_role_id_over(obj:Object):void
		{
			add_role_view.id_role_id.text=String((obj as Array)[0].role_seq_next);
		}
		/**
		 *关闭增加角色界面
		 * 
		 */
		public function closeAddRoleView(event:MouseEvent):void
		{
			PopUpManager.removePopUp(add_role_view);
		}
		/**
		 *增加角色 
		 * @param evt
		 * 
		 */
		public function addRole(evt:MouseEvent):void
		{
			if(add_role_view.id_role_name.text=="")
				BigTips.showTip('请输入角色名称', add_role_view.id_role_name, 'role_name_is_null');
			else
				BigTips.closeTip('role_name_is_null');
			
			if(add_role_view.id_role_desc.text=="")
				BigTips.showTip('请输入角色说明', add_role_view.id_role_desc, 'role_desc_is_null');
			else
				BigTips.closeTip('role_desc_is_null');
			var obj:Object=new Object();
			obj.role_id=add_role_view.id_role_id.text;
			obj.name=add_role_view.id_role_name.text;
			obj.role_desc=add_role_view.id_role_desc.text;
			obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_info[0].staff_id;
			send_note(add_role, obj);
		}
		public function big_do_add_role_over(obj:Object):void
		{
			send_note(get_role, BigMain.i_BigLoginProxy.staff_info[0].staff_id)
			PopUpManager.removePopUp(add_role_view);
		}
	}
}