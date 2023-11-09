
# NOTE
1) Color: http://ingiacong.co/bang-code-mau/
2) Icon: https://icons8.com/, https://www.flaticon.com/
3) CSS: https://xuanthulab.net/thuoc-tinh-font-family-css.html, https://www.codehub.com.vn/CSS-Co-Ban
# Transparent background
<pre>
background: transparent;
</pre>
# QComboBox

QComboBox{

	background-color: rgb(27, 29, 35);
	border-radius: 5px;
	border: 2px solid rgb(27, 29, 35);
	padding: 5px;
	padding-left: 10px;
}

QComboBox:hover{

	border: 2px solid rgb(64, 71, 88);
}
QComboBox QAbstractItemView {

	color: rgb(255, 255, 255);	
	background-color: rgb(27, 29, 35);
	padding: 10px;
	selection-background-color: rgb(85, 170, 255);
}
QComboBox::drop-down {

	subcontrol-origin: padding;
	subcontrol-position: top right;
	width: 25px; 
	border-left-width: 3px;
	border-left-color: rgba(39, 44, 54, 150);
	border-left-style: solid;
	border-top-right-radius: 3px;
	border-bottom-right-radius: 3px;	
	background-image: icons/16x16/cil-arrow-bottom.png;
	background-position: center;
	background-repeat: no-reperat;
 }

## QSlider 
QSlider::groove:horizontal {

    border-radius: 1px;
    height: 7px;
    margin: 0px;
    background-color:  rgb(52, 59, 72);
}
QSlider::groove:horizontal:hover {

    background-color:  rgb(22, 22, 22);
}
QSlider::handle:horizontal {

    background-color: rgb(85, 170, 255);
    border: none;
    height: 20px;
    width: 20px;
    margin: -20px 0;
    border-radius: 10px;
    padding: -10px 0px;
}
QSlider::handle:horizontal:hover {
<pre>
    background-color: rgb(155, 180, 255);
</pre>
}

QSlider::handle:horizontal:pressed {

    background-color: rgb(155, 180, 255);
}
# QGroupBox

QGroupBox{
    <pre>
    border:2px solid gray;
    border-radius:5px;
    margin-top: 1ex;
    background-color: rgb(39, 44, 54);
    </pre>
} 

QGroupBox::title{
    <pre>
    font: 12pt "Segoe UI";
    subcontrol-origin: margin;
    subcontrol-position:top left;
    padding:0 3px;
    </pre>
}
background-color: transparent;

# Button
QPushButton {
	<pre>
	color: rgb(255, 255, 255);
    border: 2px solid  rgb(11, 255, 227);
    border-radius: 20px;
    background-color: rgb(52, 59, 72);
	</pre>
}
QPushButton:hover {
	<pre>
	color: rgb(255, 255, 255);
	background-color: rgb(161, 161, 161);
    border: 2px solid rgb(109, 182, 168);
    border-radius: 20px; 
	</pre>

}
QPushButton:pressed { 
	<pre>
	color: rgb(255, 255, 255);
    background-color: rgb(35, 40, 49); 
    border: 2px solid rgb(43, 50, 61);
	</pre>
}