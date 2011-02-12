package bigzhu
{
        import bigzhu.Public;

        import flash.events.Event;
        import flash.events.IOErrorEvent;
        import flash.events.ProgressEvent;
        import flash.events.SecurityErrorEvent;
        import flash.net.ObjectEncoding;
        import flash.net.Socket;
        import flash.system.Security;

        import mx.controls.Alert;


        public class SocketBig extends BaseBig
        {
                public var socket:Socket = new Socket();
                public const HOST:String = '127.0.0.1';
                public const PORT:int = 8002;

                public var show_tip:Object = new Object();

                public function SocketBig(obj:Object=null)
                {
                        super(obj);
                        socket.timeout = 5000;
                        socket.objectEncoding = ObjectEncoding.AMF3;
                        addEventListener_();
                        socket.connect(HOST, PORT);
                        BaseBig.socket_big = this;
                }

                public function connect(event:Event, host:String, port:int):void
                {
                        socket.connect(host, port);
                }

                public function addEventListener_():void
                {
                        socket.addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
                        socket.addEventListener(SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler);

                        socket.addEventListener(Event.CONNECT, connectHandler);
                        socket.addEventListener(Event.CLOSE, closeHandler);
                        socket.addEventListener(ProgressEvent.SOCKET_DATA, readServerData);
                }


                public function write(obj:Object): void
                {
                        socket.writeObject(obj);
                        socket.flush();
                }


                private function securityErrorHandler(event:SecurityErrorEvent):void 
                {
                        var status:Object = new Object();
                        status.status = 'error';

                        show_tip.info = '安全问题连接后台未成功: '+event.text;
                        show_tip.comp = bigzhu_;

                        status.show_tip = show_tip;
                        send_note(STATUS_CHANGE, status);

                        Public.timeCall(3000, 1, connect, HOST, PORT);
                }

                private function ioErrorHandler(event:IOErrorEvent):void 
                {
                        var status:Object = new Object();
                        status.status = 'error';

                        show_tip.info = '连接后台未成功: '+event.text;

                        status.show_tip = show_tip;
                        send_note(STATUS_CHANGE, status);

                        Public.timeCall(3000, 1, connect, HOST, PORT);

                        //			socket.connect(HOST, PORT);
                }

                public function connectHandler(event:Event):void
                {
                        var status:Object = new Object();
                        status.status = 'ok';

                        send_note(STATUS_CHANGE, status);
                        send_note(CLEAN_TIP);
                        //			show_tip.info = '连接到后台';
                        //			show_tip.comp = bigzhu_;			//			send_note(SHOW_TIP, show_tip)			
                        //			Alert.show('连到服务器'+_host+':'+_port);
                }

                public function closeHandler(event:Event):void 
                {
                        var status:Object = new Object();
                        status.status = 'error';

                        show_tip.info = '连接关闭';

                        status.show_tip = show_tip;			
                        send_note(STATUS_CHANGE, status);

                        Public.timeCall(8000, 1, connect, HOST, PORT);
                }

                public function readServerData(event:ProgressEvent):void 
                {
                        var result:Object = socket.readObject();
                        if(result.note == SHOW_TIP)
                        {
                                show_tip.info = result.value as String;
                                show_tip.comp = bigzhu_;
                                send_note(SHOW_TIP, show_tip);

                                return;
                        }
                        send_note(result.note, result.value)
                }		
        }
}
