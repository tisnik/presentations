import QtQuick 2.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    Rectangle {
        id: r1
        width: 160
        height: 160
        color: "red"
        opacity: 0.5
        rotation: 45
        anchors.left: parent.left
        anchors.bottom: parent.bottom
    }

    Component.onCompleted: {
        console.log("ok, everything is prepared");
    }
}
