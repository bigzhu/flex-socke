package bigzhu_old
{
	import flash.events.Event;
	
	import mx.controls.Tree;
	import mx.events.ListEvent;
	
	
	public class BigPrivilege extends BigClass
	{
		public function BigPrivilege()
		{
			super();
			crm.id_privilge.labelFunction=treeLabel;
			crm.id_privilge.addEventListener(ListEvent.ITEM_CLICK, clickPrivilege); 
		}
		public function big_do_get_privilege_over(obj:Object):void
		{
			crm.id_privilge.dataProvider=obj;
			BigPublic.expandTree(crm.id_privilge);
		}
		/**
		 *控制什么作为权限树名称显示 
		 * @param item
		 * @return 
		 * 
		 */
		public function treeLabel( item:Object ):String
		{
			//return item.privilege_name;
			if (item.hasOwnProperty("@privilege_name"))
				return item.@privilege_name;
			else
				return null;
		}
		/**
		 *点击权限树后的事件处理 
		 * @param event
		 * 
		 */
		private function clickPrivilege(event:Event):void
		{
			var oItem:Object;
			oItem = Tree(event.target).selectedItem as Object;
			
			//机构管理
			if(oItem.@privilege_id=="org")
			{
				crm.id_main_view.selectedChild=crm.id_main_view.id_nav_org;
				if(BigMain.i_BigOrgProxy.org==null)
				{
					var obj:Object=new Object();
					obj.id=BigMain.i_BigLoginProxy.staff_id;
					send_note(get_org, obj);
				}
			}
				//角色管理
			else if(oItem.@privilege_id=="role")
			{
				crm.id_main_view.selectedChild=crm.id_main_view.id_nav_role;
				if(BigMain.i_BigRoleProxy.role==null)
					send_note(get_role, BigMain.i_BigLoginProxy.staff_info[0].staff_id);
			}
				//零售店管理
			else if(oItem.@privilege_id=="retail")
			{
				crm.id_main_view.selectedChild=crm.id_main_view.id_nav_retail;
				if(BigMain.i_BigOrgProxy.org==null)
				{
					obj=new Object();
					obj.id=BigMain.i_BigLoginProxy.staff_id;
					send_note(get_org, obj);
				}
			}
				//报表
			else if(oItem.@privilege_id=="report")
			{
				crm.id_main_view.selectedChild=crm.id_main_view.id_nav_report;
				if(BigMain.i_BigOrgProxy.org==null)
				{
					obj=new Object();
					obj.id=BigMain.i_BigLoginProxy.staff_id;
					send_note(get_org, obj);
				}
			}
			
		}
	}
}
