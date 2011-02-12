package bigzhu_old
{
	import big_component.*;
	
	import flash.events.ContextMenuEvent;
	import flash.events.MouseEvent;
	
	import mx.collections.*;
	import mx.containers.Accordion;
	import mx.controls.Button;
	import mx.controls.Tree;
	import mx.managers.PopUpManager;
	
	public class BigOrg extends BigClass
	{
		public var oper_accrodion:Accordion;
		//区域管理树
		public var  org_tree:Tree;
		//增加机构管理页面
		public var add_org_view:AddOrg;
		//增加客户经理
		public var add_account_manager_view:AddAccountManager;
		//增加零售店
		public var add_retail_view:AddRetail;
		//删除机构密码检查页面
		public var del_org_check_passwd_view:CheckPassword;
		
		public function BigOrg()
		{
			super();
			
			org_tree=crm.id_main_view.id_org.id_org_tree;
			oper_accrodion=crm.id_main_view.id_org.id_accordion;
			
			org_tree.labelFunction=BigPublic.treeLabel;
			org_tree.iconFunction=BigPublic.iconFun;
			org_tree.addEventListener(MouseEvent.CLICK, showAccordion);
			//初始化组件
			add_org_view=new AddOrg();
			del_org_check_passwd_view=new CheckPassword();
			add_account_manager_view=new AddAccountManager();
			add_retail_view=new AddRetail();
		}
		
		public function big_do_del_org_over(obj:*):void
		{
			oper_accrodion.removeAllChildren();
			var o_staff:Object=new Object();
			o_staff.id=BigMain.i_BigLoginProxy.staff_id;
			send_note(get_org,o_staff)
		}
		public function showAccordion(event:MouseEvent):void
		{
			var obj:Object=org_tree.selectedItem;
			//点击区域
			if(obj.@type=='org')
			{
				oper_accrodion.removeAllChildren();
				
				//删除区域
				oper_accrodion.addChild(del_org_check_passwd_view);
				var del_obj:Object=new Object();
				del_obj.id=String(obj.@id);
				del_obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_id;	
				
				del_org_check_passwd_view.label='删除 '+obj.@name +'(需要输入密码验证)';
				del_org_check_passwd_view.note_name=del_org;
				del_org_check_passwd_view.obj=del_obj;
				//增加区域
				oper_accrodion.addChild(add_org_view);
				add_org_view.label='添加区域';
				add_org_view.id_parent_org_name.text=obj.@name;
				add_org_view.id_parent_org_id.text=obj.@id;
				(add_org_view.id_add as mx.controls.Button).addEventListener(MouseEvent.CLICK, addOrg);	
				//添加客户经理
				oper_accrodion.addChild(add_account_manager_view);
				add_account_manager_view.label='添加客户经理';
				add_account_manager_view.id_parent_name.text=obj.@name;
				add_account_manager_view.id_parent_org_id.text=obj.@id;
				(add_account_manager_view.id_add as mx.controls.Button).addEventListener(MouseEvent.CLICK, addAccountManager);	
				//选中哪个
				oper_accrodion.selectedChild=add_account_manager_view;
			}
			else if(obj.@type=='account_manager')
			{
				oper_accrodion.removeAllChildren();
				//删除
				oper_accrodion.addChild(del_org_check_passwd_view);
				
				var del_am_obj:Object=new Object();
				del_am_obj.id=String(obj.@id);
				del_am_obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_id;	
				
				del_org_check_passwd_view.label='删除 '+obj.@name +'(需要输入密码验证)';
				del_org_check_passwd_view.note_name=del_org;
				del_org_check_passwd_view.obj=del_am_obj;
				
				//添加临售店
				oper_accrodion.addChild(add_retail_view);
				add_retail_view.label='添加零售店';
				add_retail_view.id_parent_name.text=obj.@name;
				add_retail_view.id_parent_org_id.text=obj.@id;
				(add_retail_view.id_add as mx.controls.Button).addEventListener(MouseEvent.CLICK, addRetail);	
				
				oper_accrodion.selectedChild=add_retail_view;
			}
			else if(obj.@type=='retail')
			{
				oper_accrodion.removeAllChildren();
				//删除
				oper_accrodion.addChild(del_org_check_passwd_view);
				
				var del_retail_obj:Object=new Object();
				del_retail_obj.id=String(obj.@id);
				del_retail_obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_id;	
				
				del_org_check_passwd_view.label='删除 '+obj.@name +'(需要输入密码验证)';
				del_org_check_passwd_view.note_name=del_org;
				del_org_check_passwd_view.obj=del_retail_obj;
			}
			else
				oper_accrodion.removeAllChildren();
			
		}
		/**
		 *增加零售店 
		 * @param event
		 * 
		 */
		public function addRetail(event:MouseEvent):void
		{
			if(add_retail_view.id_lisence_id.text=="")
				BigTips.showTip('请输入许可证号', add_retail_view, 'lisence_id_is_null');
			else
				BigTips.closeTip('lisence_id_is_null');
			
			if(add_retail_view.id_retail_name.text=="")
				BigTips.showTip('请输入零售点', add_retail_view, 'retail_name_is_null');
			else
				BigTips.closeTip('retail_name_is_null');
			
			var obj:Object=new Object();
			obj.name=add_retail_view.id_retail_name.text;
			obj.id=add_retail_view.id_lisence_id.text;
			obj.parent_id=add_retail_view.id_parent_org_id.text;
			obj.type='retail';
			
			obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_id;
			
			send_note(add_org, obj);		
		}
		/**
		 *显示删除区域时候的密码检查 
		 * @param event
		 * 
		 */
		public function showDelBssOrgCheckPasswd(event:ContextMenuEvent):void
		{
			var obj:Object=org_tree.selectedItem;
			if(obj==null)
			{
				send_note(show_error, '请先左键点击某个区域节点,以确定要在哪个节点操作');
				return;
			}
			
			if (obj.@type!='org')
			{
				send_note(show_error, '只有区域节点才能删除区域')
				return;
			}
			var del_obj:Object=new Object();
			del_obj.org_id=String(obj.@org_id);
			del_obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_id;	
			
			if(del_org_check_passwd_view==null)
				del_org_check_passwd_view=new CheckPassword();
			PopUpManager.addPopUp(del_org_check_passwd_view, org_tree, false); 
			PopUpManager.centerPopUp(del_org_check_passwd_view);
			
			del_org_check_passwd_view.note_name=del_org;
			del_org_check_passwd_view.obj=del_obj;
		}
		/**
		 * 添加客户经理
		 * @param event
		 * 
		 */
		public function addAccountManager(event:MouseEvent):void
		{
			if(add_account_manager_view.id_account_manager_name.text=="")
				BigTips.showTip('请输入客户经理名称', add_account_manager_view.id_account_manager_name, 'account_manager_is_null');
			else
				BigTips.closeTip('account_manager_is_null');
			
			var obj:Object=new Object();
			obj.name=add_account_manager_view.id_account_manager_name.text;
			obj.parent_id=add_account_manager_view.id_parent_org_id.text;
			obj.type='account_manager';
			
			obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_id;
			send_note(add_org, obj);
		}
		/**
		 * 添加区域
		 * @param event
		 * 
		 */
		
		public function addOrg(event:MouseEvent):void
		{
			if(add_org_view.id_org_name.text=="")
				BigTips.showTip('请输入区域名称', add_org_view.id_org_name, 'org_name_is_null');
			else
				BigTips.closeTip('org_name_is_null');
			
			var obj:Object=new Object();
			obj.name=add_org_view.id_org_name.text;
			obj.parent_id=add_org_view.id_parent_org_id.text;
			obj.type='org';
			
			obj.oper_staff_id=BigMain.i_BigLoginProxy.staff_id;
			
			send_note(add_org, obj);
		}
		
		public function big_do_add_org_over(obj:*):void
		{
			var o_staff:Object=new Object();
			o_staff.id=BigMain.i_BigLoginProxy.staff_id;
			send_note(get_org, o_staff);
		}
		public function big_do_get_org_over(obj:Object):void
		{
			org_tree.dataProvider=obj;
			BigPublic.expandTree(org_tree);
		}
		

	}
}
