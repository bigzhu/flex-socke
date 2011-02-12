package bigzhu_old
{
	import bigzhu.*;
	import bigzhu_old.proxy.*;
	
	public class BigMain
	{
		public function BigMain()
		{
		}
		public static var i_BigReport :BigReport =new BigReport ();
		public static var i_BigReportProxy :BigReportProxy =new BigReportProxy ();
		
		public static var i_BigRetailProxy :BigRetailProxy =new BigRetailProxy ();
		//店铺信息
		public static var i_BigShop:BigShop=new BigShop();
		//商圈环境
		public static var i_BigBusiness:BigBusiness=new BigBusiness();
		//零售点
		public static var i_BigRetail:BigRetail=new BigRetail();
		//登录
		public static var i_BigLogin:BigLogin=new BigLogin();
		public static var i_BigLoginProxy:BigLoginProxy=new BigLoginProxy();
		//取权限
		public static var i_BigGetPrivilegeProxy:BigPrivilegeProxy=new BigPrivilegeProxy();
		public static var i_BigPrivilege:BigPrivilege=new BigPrivilege();
		//机构
		public static var i_BigOrgProxy:BigOrgProxy=new BigOrgProxy();
		public static var i_BigOrg:BigOrg=new BigOrg();
		//角色
		public static var i_BigRoleProxy:BigRoleProxy=new BigRoleProxy();
		public static var i_BigRole:BigRole=new BigRole();
		
		public static var i_BigShowError:BigShowError=new BigShowError();
		//proxy
		public static var i_BigProxy:BigProxy=new BigProxy();
		
		public static function startup():void
		{
			//			i_BigLogin=new BigLogin();
			//			 i_BigShowError=new BigShowError();
			//			//proxy
			//			i_BigProxy=new BigProxy();
			//			i_BigLoginProxy= new BigLoginProxy();
		}
	}
}