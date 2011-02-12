package bigzhu_old
{
	import big_component.*;
	
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	import mx.controls.Tree;
	import mx.events.ListEvent;
	import mx.managers.PopUpManager;
	
	
	public class BigReport extends BigClass
	{
		public var report:Report;
		public var report_tree:Tree;
		public var select_retail:SelectRetail;
		public var retail_id:String;
		public var retail_name:String;
		public function BigReport()
		{
			super();
			report=crm.id_main_view.id_report;
			retail_id='';
			select_retail=new SelectRetail();
			report_tree=new Tree();
			report_tree.width=600;
			report_tree.height=400;
			
			//			report.id_begin_date.selectedDate=new Date();	
			//			report.id_end_date.selectedDate=new Date();	
			
			report_tree.labelFunction=BigPublic.treeLabel;			
			report_tree.iconFunction=BigPublic.iconFun;		
			select_retail.addElement(report_tree);
			addEvent();
		}
		public function big_do_query_report_over(obj:Object):void
		{
			report.id_data_grid.dataProvider=obj;
			
		}
		public function big_do_get_org_over(obj:Object):void
		{
			report_tree.dataProvider=obj;
		}
		public function addEvent():void
		{
			report.id_select.addEventListener(MouseEvent.CLICK, showRetailTree);
			report_tree.addEventListener(ListEvent.ITEM_CLICK, selected_retail);
			
			report.id_query.addEventListener(MouseEvent.CLICK, query);
		}
		
		public function query(event:Event):void
		{
			if(retail_id=='')
			{
				
				BigTips.showTip("请选择要查的区域!", report.id_retail_id , "retail_id_is_null");
				return;
			}
			else
				BigTips.closeTip("retail_id_is_null");
		
			var obj:Object=new Object();
			obj.retail_id=retail_id;
			//			obj.begin_date=report.id_begin_date.text;
			//			obj.end_date=report.id_end_date.text;
			
			send_note(query_report, obj);
			
		}
		public function selected_retail(event:Event):void
		{

			retail_id=report_tree.selectedItem.@id;
			retail_name=report_tree.selectedItem.@name;
			
			report.id_retail_id.text=report_tree.selectedItem.@name+'('+report_tree.selectedItem.@id+')';
			PopUpManager.removePopUp(select_retail);
		}
		public function showRetailTree(event:Event):void
		{
			PopUpManager.addPopUp(select_retail, report, true);  
			PopUpManager.centerPopUp(select_retail);
			BigPublic.expandTree(report_tree);
		}
	}
}