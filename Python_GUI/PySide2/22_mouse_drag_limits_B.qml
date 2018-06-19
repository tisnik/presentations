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
        x: 0
        y: 0

        MouseArea {
            id: mouseArea1
            anchors.fill: parent
            drag {
                target: r1
                axis: Drag.XAndYAxis
                minimumX: 0
                maximumX: main.width - r1.width
                minimumY: 0
                maximumY: main.height - r1.height
            }
        }
    }

    Rectangle {
        id: r2
        width: 160
        height: 160
        color: "yellow"
        opacity: 0.5
        x: 80
        y: 80
        z: 1

        MouseArea {
            id: mouseArea2
            anchors.fill: parent
            drag {
                target: r2
                axis: Drag.YAxis
                minimumY: 0
                maximumY: main.height - r2.height
            }
        }
    }

    Rectangle {
        id: r3
        width: 160
        height: 160
        color: "blue"
        opacity: 0.5
        x: 160
        y: 0

        MouseArea {
            id: mouseArea3
            anchors.fill: parent
            drag {
                target: r3
                axis: Drag.XAxis
                minimumX: 0
                maximumX: main.width - r3.width
            }
        }
    }

}
