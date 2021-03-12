import sys
import io
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine
from PyQt5.QtGui import QIcon

"""
Folium in PyQt5
"""


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setWindowTitle('Kızılay Harita')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle('İzmir Kızılay Harita1 ')
        self.setWindowIcon(QIcon('Crescent.png'))

        layout = QVBoxLayout()
        self.setLayout(layout)

        import folium
        m = folium.Map(location=[38.418720, 27.129601], tiles="Stamen Terrain", zoom_start=15)
        m

        locationRedCrescent = [38.399730, 27.241565]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/Crescent3.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Ege Bölge Afet Yönetim Merkezi<br><br><br>Sorumlu:Murat Korkut</strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Ege Bölge Afet Yönetim Merkezi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        m

        locationRedCrescent = [38.428730, 27.135780]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/Crescent3.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>İzmir Kızılay<br><br><br>Sorumlu:Talha Şengül</strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="İzmir Kızılay", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        m

        locationRedCrescent = [38.462270, 27.244330]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/Crescent3.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Bornova Kızılay<br><br><br>Sorumlu:Cemil Kurkut</strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Bornova Kızılay", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        m

        locationRedCrescent = [38.456250, 27.122790]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/Crescent3.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Karşıyaka Kızılay<br><br><br>Sorumlu:Kamil Karadeniz</strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Karşıyaka Kızılay", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        m

        locationRedCrescent = [38.194640, 26.839500]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/Crescent3.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Seferihisar Kızılay<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Seferihisar Kızılay", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        m

        locationRedCrescent = [38.454120, 27.254550]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/AFADLOGO.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>İzmir Afad Genel Müdürlüğü<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="İzmir Afad", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.435070, 27.142520]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/Crescent3.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Konak Kızılay <br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Konak Kızılay", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        m

        locationRedCrescent = [38.424860, 27.133120]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/EGMLOGO.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>İzmir Emniyet Genel Müdürlüğü<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="İzmir İl Emniyet", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        m
        locationRedCrescent = [38.803719, 26.969450]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Aliağa Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Aliağa Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.385250, 27.058250]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Balçova Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Balçova Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.220840, 27.647160]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Bayındır Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Bayındır Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.464860, 27.163020]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Bayraklı Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Bayraklı Belediyesi", popup=popupRedCrescent,
                 icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [39.118950, 27.178300]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Bergama Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Bergama Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.087869, 28.209056]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Beydağ Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Beydağ Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.703470, 27.026140]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Bornova Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Bornova Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.389780, 27.164090]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Buca Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Buca Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [37.186240, 32.240700]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Çeşme Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Çeşme Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [41.258150, 26.890790]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Çiğli Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Çiğli Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [41.258150, 26.890790]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Çiğli Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Çiğli Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [39.077920, 26.969450]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Dikili Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Dikili Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.664000, 26.745130]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Foça Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Foça Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.322860, 27.129620]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Gaziemir Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Gaziemir Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.359810, 26.888040]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png', icon_size=(50, 50))
        popupRedCrescent = "<strong>Güzelbahçe Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Güzelbahçe Belediyesi", popup=popupRedCrescent,
              icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.608780, 27.063830]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Menemen Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Menemen Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.382230, 27.131260]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Karabağlar Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Karabağlar Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.515050, 26.617380]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Karaburun Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Karaburun Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.459610, 27.114440]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Karşıyaka Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Karşıyaka Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.482650, 27.354530]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Kemalpaşa Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Kemalpaşa Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [39.087540, 27.380280]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Kınık Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Kınık Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        locationRedCrescent = [38.232090, 28.205710]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Kiraz Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Kiraz Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        locationRedCrescent = [38.419320, 27.130230]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Konak Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Konak Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)
        locationRedCrescent = [38.256050, 27.130650]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Menderes Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Menderes Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.327860, 26.766370]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Urla Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Urla Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.149780, 27.361410]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Torbalı Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Torbalı Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.087670, 27.731520]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Tire Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Tire Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [37.949700, 27.369900]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Selçuk Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Selçuk Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.196860, 26.839020]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Seferihisar Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Seferihisar Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.228850, 27.974430]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                     icon_size=(50, 50))
        popupRedCrescent = "<strong>Ödemiş Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Ödemiş Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)

        locationRedCrescent = [38.396230, 26.995960]
        iconRedCrescent = folium.features.CustomIcon('C:/Users/90545/Desktop/Stuffs/belediyelogo.png',
                                                             icon_size=(50, 50))
        popupRedCrescent = "<strong>Narlıdere Belediyesi<br><br><br></strong><br>"
        folium.Marker(location=locationRedCrescent, tooltip="Narlıdere Belediyesi", popup=popupRedCrescent,
                      icon=iconRedCrescent).add_to(m)






        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')