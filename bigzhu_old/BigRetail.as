package bigzhu_old
{
	import big_component.*;
	
	import flash.events.MouseEvent;
	
	import mx.collections.ArrayCollection;
	import mx.containers.TabNavigator;
	import mx.controls.Tree;
	
	import spark.components.NavigatorContent;
	
	public class BigRetail extends BigClass
	{
		//图标
		[Embed(source="/images/head.png")]
		public var account_manager_icon:Class;
		
		[Embed(source="/images/retail.png")]
		public var retail_icon:Class;
		
		[Embed(source="/images/org.png")]
		public var org_icon:Class;
		
		public var  org_tree:Tree;
		public var tab_nav:TabNavigator;
		public var retail:Retail;
		
		public function BigRetail()
		{
			super();
			org_tree=crm.id_main_view.id_retail.id_org_tree;
			org_tree.addEventListener(MouseEvent.CLICK, showTab);
			org_tree.labelFunction=treeLabel;
			org_tree.iconFunction=iconFun;
			//三个tab窗口
			tab_nav=crm.id_main_view.id_retail.id_nav_tab;
			retail=crm.id_main_view.id_retail;
		}
		public function big_do_get_org_over(obj:*):void
		{
			org_tree.dataProvider=obj;
			BigPublic.expandTree(org_tree);
		}
		
		public function showTab(event:MouseEvent):void
		{
			var obj:Object=org_tree.selectedItem;
			//点击区域
			if(obj.@type=='retail')
			{
				retail.id_nav_tab.visible=true;
				retail.retail_name=obj.@name;
				retail.retail_id=obj.@id;
				
				var re:Object=new Object();
				re.retail_id=retail.retail_id;
				send_note(get_retail_info, re);
			}
			else
				retail.id_nav_tab.visible=false;
		}
		/**
		 *控制什么作为权限树名称显示 
		 * @param item
		 * @return 
		 * 
		 */
		public function treeLabel( item:Object ):String
		{
			if(item.@type=='account_manager')
			{
				return item.@name+'('+item.@id+')';
			}
			else
				return item.@name;
		}
		/**
		 *控制什么作为权限树图标显示 
		 * @param item
		 * @return 
		 * 
		 */
		public function iconFun(item:Object):*
		{
			if(item.@type=='account_manager')
				return account_manager_icon;
			if(item.@type=='retail')
				return retail_icon;
			if(item.@type=='org')
				return org_icon;	
		}
		
		public function big_do_get_retail_info_over(obj:*):void
		{
			BigMain.i_BigBusiness.add_detail_data(obj);
			BigMain.i_BigShop.add_detail_data(obj);
		}
	}
}
