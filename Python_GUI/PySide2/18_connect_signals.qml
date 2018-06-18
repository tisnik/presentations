import QtQuick 2.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    function onRect1Click(mouse) {
        r1.color = Qt.rgba(Math.random(), Math.random(), Math.random(), 1);
        console.log("mouse coordinates:", mouse.x, mouse.y);
    }

    function onRect1WheelRotate(wheel) {
        console.log("mouse wheel:", wheel.angleDelta.y);
        r1.rotation += wheel.angleDelta.y / 30;
    }

    function onRect2Click(mouse) {
        r2.color = Qt.rgba(Math.random(), Math.random(), Math.random(), 1);
        console.log("mouse coordinates:", mouse.x, mouse.y);
    }

    function onRect2WheelRotate(wheel) {
        console.log("mouse wheel:", wheel.angleDelta.y);
        r2.rotation += wheel.angleDelta.y / 30;
    }

    function onRect3Click(mouse) {
        r3.color = Qt.rgba(Math.random(), Math.random(), Math.random(), 1);
        console.log("mouse coordinates:", mouse.x, mouse.y);
    }

    function onRect3WheelRotate(wheel) {
        console.log("mouse wheel:", wheel.angleDelta.y);
        r3.rotation += wheel.angleDelta.y / 30;
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
        mouseArea1.clicked.connect(onRect1Click)
        mouseArea1.wheel.connect(onRect1WheelRotate)
        mouseArea2.clicked.connect(onRect2Click)
        mouseArea2.wheel.connect(onRect2WheelRotate)
        mouseArea3.clicked.connect(onRect3Click)
        mouseArea3.wheel.connect(onRect3WheelRotate)
    }
}
