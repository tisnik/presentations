import QtQuick 1.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    Rectangle {
        id: r1
        width: 100
        height: 100
        color: "red"
        anchors.verticalCenter: main.verticalCenter
    }

    Rectangle {
        id: r2
        width: 100
        height: 100
        color: "blue"
        anchors.left: r1.right
    }

    Rectangle {
        id: r3
        width: 100
        height: 100
        color: "yellow"
        anchors.left: r2.right
        anchors.top: r2.bottom
    }
}
