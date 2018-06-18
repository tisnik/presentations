import QtQuick 2.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    function onRectClick(rectangle, mouse) {
        rectangle.color = Qt.rgba(Math.random(), Math.random(), Math.random(), 1);
        console.log("mouse coordinates:", mouse.x, mouse.y);
    }

    function onRectWheelRotate(rectangle, wheel) {
        console.log("mouse wheel:", wheel.angleDelta.y);
        rectangle.rotation += wheel.angleDelta.y / 30;
    }

    Rectangle {
        id: r1
        width: 160
        height: 160
        color: "red"
        opacity: 0.5
        rotation: 45
        anchors.left: parent.left
        anchors.bottom: parent.bottom

        MouseArea {
            id: mouseArea1
            anchors.fill: parent
        }
    }

    Rectangle {
        id: r2
        width: 160
        height: 160
        color: "yellow"
        opacity: 0.5
        z: 1
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top

        MouseArea {
            id: mouseArea2
            anchors.fill: parent
        }
    }

    Rectangle {
        id: r3
        width: 160
        height: 160
        color: "blue"
        opacity: 0.5
        rotation: 45
        anchors.right: parent.right
        anchors.bottom: parent.bottom

        MouseArea {
            id: mouseArea3
            anchors.fill: parent
        }
    }

    Component.onCompleted: {
        console.log("completed")
        mouseArea1.clicked.connect(function(event) {onRectClick(r1, event)})
        mouseArea2.clicked.connect(function(event) {onRectClick(r2, event)})
        mouseArea3.clicked.connect(function(event) {onRectClick(r3, event)})

        mouseArea1.wheel.connect(function(event) {onRectWheelRotate(r1, event)})
        mouseArea2.wheel.connect(function(event) {onRectWheelRotate(r2, event)})
        mouseArea3.wheel.connect(function(event) {onRectWheelRotate(r3, event)})
    }
}
