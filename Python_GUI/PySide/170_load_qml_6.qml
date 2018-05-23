import QtQuick 1.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"
    anchors.fill: parent
    focus: true
    Keys.onDigit1Pressed: r1.color = "red"
    Keys.onDigit2Pressed: r2.color = "cyan"
    Keys.onDigit3Pressed: r3.color = "yellow"

    Rectangle {
        id: r1
        width: 100
        height: 100
        color: "gray"
        anchors.verticalCenter: main.verticalCenter
        MouseArea {
            anchors.fill: parent
            onClicked: parent.color = "magenta"
        }
    }

    Rectangle {
        id: r2
        width: 100
        height: 100
        color: "gray"
        anchors.left: r1.right
        MouseArea {
            anchors.fill: parent
            onClicked: parent.color = "blue"
        }
    }

    Rectangle {
        id: r3
        width: 100
        height: 100
        color: "gray"
        anchors.left: r2.right
        anchors.top: r2.bottom
        MouseArea {
            anchors.fill: parent
            onClicked: parent.color = "green"
        }
    }
}
