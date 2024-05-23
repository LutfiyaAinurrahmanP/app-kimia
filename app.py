import streamlit as st
import numpy as np

# Menampilkan  halaman dashboard
def dashboard():
    st.markdown('<h1 style="color: #DA0C81;">Aplikasi Penentu pH Larutan</h1>', unsafe_allow_html=True)
    st.write('Halo **users**, selamat datang di web kelompok 11'"\N{winking face}")
    st.write('Aplikasi <span style="color: #DA0C81;">**pHlytics**</span> ini dapat digunakan untuk menghitung pH dari suatu larutan disertai dengan sifat larutan tersebut dengan menginput konsentrasi (molaritas)', unsafe_allow_html=True)
    image1 = st.image("asset/header.png", use_column_width=True, width=None, clamp=False)

def rumus_asam_kuat():
    html_text = """
    <p>
    <strong>HCl→H<sup>+</sup> + Cl<sup>-</sup></strong>
    </p>
    """
    return html_text

def rumus_asam_lemah():
    html_text = """
    <p>
    <strong>CH<sub>3</sub>COOH↔CH<sub>3</sub>COO<sup>-</sup> + H<sup>+</sup></strong>
    </p>
    """
    return html_text

def rumus_basa_kuat():
    html_text = """
    <p>
    <strong>NaOH→Na<sup>+</sup>+OH<sup>-</sup></strong>
    </p>
    """
    return html_text

def rumus_basa_lemah():
    html_text = """
    <p>
    <strong>NH<sub>3</sub>+H<sub>2</sub>O↔NH<sub>4</sub><sup>+</sup> + OH<sup>-</sup></strong>
    </p>
    """
    return html_text

# Menampilkan halaman kalkulator
def kalkulator():

    # Tambahkan pilihan tambahan di sidebar setelah memilih kalkulator
    st.sidebar.subheader("Pilihan Kalkulator:")
    selected_calc_option = st.sidebar.selectbox(
        'Pilih:',
        ("Pilih Penentuan", "Penentuan Nilai pH", "Penentuan Indikator")
    )

    # Tidak memilih apa apa, menampilkan peringatan
    if selected_calc_option == "Pilih Penentuan":
        st.sidebar.warning("Harap pilih penentuan terlebih dahulu!")
    
    # Jika memilih menu Penentuan Nilai pH
    elif selected_calc_option == "Penentuan Nilai pH":
        st.markdown('<h1 style="color: #DA0C81;">Penentuan Nilai pH</h1>', unsafe_allow_html=True)
        lar = st.text_input("Nama Larutan yang akan dihitung pH-nya : ")
        option = st.selectbox("Jenis Larutan:", ["Pilih Jenis Larutan", "Asam Kuat", "Basa Kuat", "Asam Lemah", "Basa Lemah"])

        # Logika pilih larutan
        if option == "Pilih Jenis Larutan":
            st.warning("Pilih jenis larutan terlebih dahulu")
        else:
            jumlah_digit = 4
            cons = st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
            
            # Pilihan Asam Kuat dan Basa Kuat
            if option in ["Asam Kuat", "Basa Kuat"]:
                jumlah_digit1 = 4
                val = st.number_input(f'Masukkan nilai valensi larutan', format='%.'+str(jumlah_digit)+'f')
                # Asam Kuat
                if option == "Asam Kuat":
                    H = cons * val
                    pH = -(np.log10(H))
                    if st.button('Hitung'):
                        if cons == 0 or val == 0:
                            st.warning("Harap untuk tidak memberi angka 0 pada perhitungan")
                        else :
                            st.balloons()
                            st.success(f'pH Larutan {lar} yang merupakan {option} adalah: {round(pH,2)}')
                # Basa Kuat
                elif option == "Basa Kuat":
                    OH = cons * val
                    POH = (np.log10(OH))
                    pH = 14 - POH
                    if st.button('Hitung'):
                        if cons == 0 or val == 0:
                            st.warning("Harap untuk tidak memberi angka 0 pada perhitungan")
                        else :
                            st.balloons()
                            st.success(f'pH Larutan {lar} yang merupakan {option} adalah: {round(pH,2)}')

            # Pilihan Asam Lemah dan Basa Lemah
            elif option in ["Asam Lemah", "Basa Lemah"]:
                a = cons * (1.8 * 10**(-5))
                # Asam Lemah
                if option == "Asam Lemah":
                    H = np.sqrt(a)
                    pH = -(np.log10(H))
                    if st.button('Hitung'):
                        if cons == 0:
                            st.warning("Harap untuk tidak memberi angka 0 pada perhitungan")
                        else :
                            st.balloons()
                            st.success(f'pH Larutan {lar} yang merupakan {option} adalah: {round(pH,2)}')
                # Basa Lemah
                elif option == "Basa Lemah":
                    OH = np.sqrt(a)
                    POH = - (np.log10(OH))
                    pH = 14 - POH
                    if st.button('Hitung'):
                        if cons == 0:
                            st.warning("Harap untuk tidak memberi angka 0 pada perhitungan")
                        else :
                            st.balloons()
                            st.success(f'pH Larutan {lar} yang merupakan {option} adalah: {round(pH,2)}')

    # Jika memilih Penentuan Indikator   
    elif selected_calc_option == "Penentuan Indikator":
        st.markdown('<h1 style="color: #DA0C81;">Penentuan Indikator</h1>', unsafe_allow_html=True) 
        ph_value = st.number_input("Masukkan nilai pH anda :", min_value=3.0, max_value=10.1)

        # Jika memasukkan 3.1 - 4.4
        if 3.1 <= ph_value <= 4.4:
            st.success("Indikator yang cocok untuk pH anda adalah: Sindur Metil")
            if st.button("Pelajari Tentang Sindur Metil"):
                st.markdown("""
                    Indikator Sindur Metil adalah senyawa kimia yang digunakan sebagai indikator pH pada larutan asam atau netral dalam rentang pH 3,1-4,4.
                    berikut adalah beberapa fakta tentang sindur metil:
                    
                    - **Nama Kimia:** Sindur metil juga dikenal sebagai 4-dimetilaminoazobenzena atau merah CIB-3.
                    
                    - **Sifat Warna:** Senyawa ini memiliki sifat warna yang unik; berwarna merah dalam suasana asam dan berubah menjadi kuning dalam suasana basa.
                    
                    - **Indikator pH:** Sindur metil digunakan sebagai indikator pH dalam titrasi asam-basa. Perubahan warna yang ditunjukkan oleh sindur metil digunakan untuk menentukan titik akhir titrasi.
                    
                    - **Spektrum Absorpsi:** Sindur metil menunjukkan puncak absorpsi dalam spektrum UV-Vis pada panjang gelombang sekitar 520 nm.
                    
                    - **Aplikasi:** Selain sebagai indikator pH, sindur metil juga digunakan dalam pewarnaan histologi untuk mewarnai jaringan biologis dalam mikroskopi.
                    
                    - **Keamanan:** Meskipun digunakan dalam banyak aplikasi laboratorium, sindur metil harus ditangani dengan hati-hati karena sifatnya yang beracun dan kemungkinan pencemaran lingkungan.
                    
                    - **Penggunaan Historis:** Sindur metil telah digunakan dalam berbagai aplikasi sejak awal abad ke-20 dan tetap menjadi salah satu indikator pH yang penting dan umum digunakan hingga saat ini.
                    """)
        
        # Jika memasukkan 4.2 - 6.3
        elif 4.2 <= ph_value <= 6.3:
            st.success("Indikator yang cocok untuk pH anda adalah: Indikator Metil Merah")
            if st.button("Pelajari Tentang Indikator Metil Merah"):
                st.markdown("""        
                    Indikator metil merah adalah senyawa kimia yang digunakan sebagai indikator pH pada larutan asam atau netral dalam rentang pH 4,2-6,3.
                    berikut adalah beberapa fakta tentang indikator metil merah:
                    
                    - **Nama Kimia:** Metil merah juga dikenal sebagai p-[(dimetilamino)fenil]-diazenilbenzena atau C.I. 13020.
                    
                    - **Perubahan Warna:** Metil merah memiliki sifat warna yang unik: berwarna merah dalam suasana asam dan berubah menjadi kuning saat larutan menjadi basa. Perubahan warna ini terjadi di sekitar pH 4,4 hingga 6,2.
                    
                    - **Penggunaan:** Metil merah sering digunakan sebagai indikator pH dalam titrasi asam-basa, terutama dalam titrasi asam lemah dengan basa kuat atau dalam titrasi alkali dengan asam lemah.
                    
                    - **Titik Perubahan Warna:** Titik perubahan warna metil merah sedikit lebih rendah daripada fenolftalein, sehingga metil merah lebih cocok untuk titrasi asam yang lebih lemah.
                    
                    - **Kepekaan Terhadap Cahaya:** Metil merah rentan terhadap kerusakan oleh cahaya matahari dan sinar UV, sehingga harus disimpan dalam botol berwarna gelap untuk menjaga kestabilannya.
                    """)
                
        # Jika memasukkan 6.0 - 7.6
        elif 6.0 <= ph_value <= 7.6:
            st.success("Indikator yang cocok untuk pH anda adalah: Indikator Bromtimol Blue")
            if st.button("Pelajari Tentang Indikator Bromtimol Blue"):
                st.markdown("""        
                    Indikator bromtimol blue adalah senyawa kimia yang digunakan sebagai indikator pH dalam titrasi asam-basa dalam rentang pH 6,0-7,6.
                    berikut adalah beberapa fakta tentang indikator bromtimol blue:
                    
                    - **Nama Kimia:** Bromtimol blue juga dikenal sebagai 3',3'',5',5''-tetrabromofenolsulfonftalein atau C.I. 42090.
                    
                    - **Perubahan Warna:** Bromtimol blue memiliki sifat warna yang unik: berwarna biru dalam suasana basa, hijau dalam suasana netral, dan berubah menjadi kuning ketika larutan menjadi asam. Perubahan warna ini terjadi di sekitar pH 6,0 hingga 7,6.
                    
                    - **Kepekaan Terhadap Cahaya:** Seperti banyak indikator lainnya, bromtimol blue rentan terhadap kerusakan oleh cahaya matahari dan sinar UV, sehingga harus disimpan dalam botol berwarna gelap untuk menjaga kestabilannya.
                    
                    - **Penggunaan:** Bromtimol blue digunakan sebagai indikator pH dalam titrasi asam-basa, terutama dalam titrasi asam kuat dengan basa kuat atau dalam titrasi asam lemah dengan basa kuat.
                    
                    - **Penggunaan Lain:** Selain sebagai indikator pH, bromtimol blue juga digunakan dalam biologi sebagai penanda untuk mengidentifikasi zona pH dalam elektroforesis gel agarosa.
                    """)

        # Jika memasukkan 8.2 - 10
        elif 8.2 <= ph_value <= 10:
            st.success("Indikator yang cocok untuk pH anda adalah: Indikator Fenolftalein")
            if st.button("Pelajari Tentang Indikator Fenolftalein"):
                st.markdown("""        
                Indikator fenolftalein adalah senyawa kimia yang digunakan sebagai indikator pH dalam titrasi asam-basa dalam rentang pH 8,2-10.
                berikut adalah beberapa fakta tentang indikator fenolftalein:
                
                - **Nama Kimia:** Fenolftalein memiliki nama kimia 3,3-bis(4-hidroksifenil)-2H-isobenzofuran-1-on.
                
                - **Perubahan Warna:** Fenolftalein tidak berwarna dalam suasana asam, tetapi berubah menjadi merah muda hingga merah dalam suasana basa.
                
                - **Titik Perubahan Warna:** Perubahan warna fenolftalein terjadi di sekitar pH 8,2 hingga 10,0. Di bawah pH 8,2, fenolftalein tetap tidak berwarna, sedangkan di atas pH 10,0, fenolftalein menjadi merah.
                
                - **Penggunaan Umum:** Fenolftalein adalah indikator pH yang sangat umum digunakan dalam laboratorium kimia, terutama dalam titrasi asam-basa. Perubahan warna fenolftalein menunjukkan titik akhir titrasi, di mana asam dan basa telah bereaksi sepenuhnya.
                
                - **Kerusakan:** Fenolftalein rentan terhadap kerusakan oleh sinar UV dan dapat memudar dari paparan cahaya matahari yang berlebihan.
                """)

        # Jika nilai tidak sesuai dengan range yang ditentukan seperti diatas
        else:
            st.warning("""
                    Nilai pH yang anda masukkan tidak termasuk dalam indikator apapun
                    """)

# Perhitungan pada pH
def hitung_pH(nama_senyawa, jenis_senyawa, konsentrasi, valensi):
    # Hitung pH dan indikator berdasarkan Jenis Larutan
    pH = None
    indikator = None
    if jenis_senyawa == "Asam Kuat":
        pH = -np.log10(konsentrasi)
        indikator = "Fenolftalein"
    elif jenis_senyawa == "Asam Lemah":
        pass
    elif jenis_senyawa == "Basa Kuat":
        pOH = -np.log10(konsentrasi)
        pH = 14 - pOH
        indikator = "Fenolftalein"
    elif jenis_senyawa == "Basa Lemah":
        pass

    return pH, indikator

# Menampilkan halaman tentang sistem
def tentang_sistem():
    st.markdown('<h1 style="color: #DA0C81;">Tentang Sistem</h1>', unsafe_allow_html=True)
    st.markdown('<p><strong style="color: #E95793;">Nama Projek:</strong> Aplikasi Penentu pH Larutan dan Penentu Indikator</p>', unsafe_allow_html=True)
    st.markdown('<p><strong style="color: #E95793;">Nama Sistem:</strong> pHlytics</p>', unsafe_allow_html=True)
    st.markdown('<p><strong style="color: #E95793;">Penjelasan Sistem:</strong> aplikasi ini  dapat digunakan untuk menentukan nilai pH dengan cara menginput konsentrasi dan valensi dari suatu larutan, serta dapat menentukan indikator dengan cara menginput nilai dari pH suatu larutan</p>', unsafe_allow_html=True)
    st.markdown('<p><strong style="color: #E95793;">Input:</strong> Nama senyawa (masukkan sendiri), Konsentrasi larutan dalam molaritas dan valensi senyawa</p>', unsafe_allow_html=True)
    st.markdown('<p><strong style="color: #E95793;">Output:</strong> pH, sifat larutan nya, indikator yang cocok.</p>', unsafe_allow_html=True)

# Menampilkan halaman about us
def about_us():
    st.markdown('<h1 style="color: #DA0C81;">About Us</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #E95793;"><strong>Biodata Kelompok (Kelas 1C-Analisis Kimia):</strong></p>', unsafe_allow_html=True)
    st.write('1. Adhisurya Pratama (2360057)')
    st.write('2. Cahya Bintang Gagana Yuliano (2360089)')
    st.write('3. Intan Cahyaningtyas (2360147)')
    st.write('4. Shintha Aulia (2360261)')
    st.markdown('<p style="color: #E95793;"><strong>Tentang Kami:</strong></p>', unsafe_allow_html=True)
    st.markdown("""
    Kami adalah tim pengembang aplikasi ini. Kami adalah Mahasiswa/i Politeknik AKA Bogor yang memiliki minat dalam ilmu kimia. Kami mengembangkan aplikasi ini sebagai proyek untuk mempelajari lebih lanjut tentang konsep pH dan indikator pH. Kami harap aplikasi ini dapat bermanfaat bagi Anda dalam memahami konsep tersebut.
    """)
    
# Menampilkan penjelasan
def penjelasan():

    # Tambahkan pilihan tambahan di sidebar setelah memilih kalkulator
    st.sidebar.subheader("Pilihan Penjelasan:")
    selected_calc_option = st.sidebar.selectbox(
        'Pilih:',
        ("Pilih Penjelasan", "Asam dan Basa", "Indikator")
    )

      # Tidak memilih apa apa, menampilkan peringatan
    if selected_calc_option == "Pilih Penjelasan":
        st.sidebar.warning("Harap pilih penjelasan terlebih dahulu!")
  
    elif selected_calc_option == "Asam dan Basa":
        st.markdown('<h1 style="color: #DA0C81;">Penjelasan Asam dan Basa</h1>', unsafe_allow_html=True)
        tabs = st.tabs(['Asam Kuat', 'Asam lemah', 'Basa Kuat', 'Basa Lemah'])
        
        # Pilihan 0 / pertama
        # karena array dimulai dari 0 bukan 1
        with tabs[0]:
            st.markdown('<h2><strong style="color: #E95793;">Asam Kuat</strong></h2>', unsafe_allow_html=True)

            st.markdown("""
            Asam Kuat: Asam kuat adalah asam yang sepenuhnya terionisasi dalam larutan air, yang berarti hampir semua molekul asam melepaskan ion hidrogen (H⁺) ke dalam larutan. Contoh umum asam kuat termasuk asam klorida (HCl), asam sulfat (H₂SO₄), dan asam nitrat (HNO₃). Dalam larutan air, reaksi ionisasi asam kuat adalah sebagai berikut: 
            """)
            st.markdown(rumus_asam_kuat(), unsafe_allow_html=True)
            st.markdown("""          
            Karakteristik Asam Kuat:
                        
            - **Ionisasi Lengkap:** Semua molekul asam terionisasi.
                        
            - **Ka Besar:** Nilai konstanta disosiasi asam (Ka) sangat besar.
                        
            - **Ph:** Larutan asam kuat memiliki pH yang sangat rendah.
                        
            - **Kekuatan Reaksi:** Reaksi dengan basa menghasilkan garam dan air secara sempurna.
            """)
        
        # Pilihan 1 / kedua
        with tabs[1]:
            st.markdown('<h2><strong style="color: #E95793;">Asam Lemah</strong></h2>', unsafe_allow_html=True)

            st.markdown("""
            Asam Lemah: Asam lemah adalah asam yang hanya sebagian terionisasi dalam larutan air, yang berarti hanya sebagian kecil molekul asam melepaskan ion hidrogen (H⁺) ke dalam larutan. Contoh asam lemah termasuk asam asetat (CH₃COOH), asam karbonat (H₂CO₃), dan asam fosfat (H₃PO₄). Reaksi ionisasi asam lemah adalah sebagai berikut: 
            """)
            st.markdown(rumus_asam_lemah(), unsafe_allow_html=True)                        
            st.markdown(""" 
            Karakteristik Asam Lemah:
                        
            - **Ionisasi Parsial:** Hanya sebagian molekul asam terionisasi.
                        
            - **Ka Kecil:** Nilai konstanta disosiasi asam (Ka) kecil.
                        
            - **Ph:** Larutan asam lemah memiliki pH yang lebih tinggi dibandingkan asam kuat dengan konsentrasi yang sama.
                        
            - **Kekuatan Reaksi:** Reaksi dengan basa menghasilkan garam dan air, tetapi tidak sepenuhnya.
            """)
        
        
        # Pilihan 2 / ketiga
        with tabs[2]:
            st.markdown('<h2><strong style="color: #E95793;">Basa Kuat</strong></h2>', unsafe_allow_html=True)

            st.markdown("""
            Basa Kuat: Basa kuat adalah basa yang sepenuhnya terionisasi dalam larutan air, sehingga setiap molekul basa melepaskan ion hidroksida (OH⁻) ke dalam larutan. Contoh basa kuat termasuk natrium hidroksida (NaOH), kalium hidroksida (KOH), dan kalsium hidroksida (Ca(OH)₂). Reaksi ionisasi basa kuat adalah sebagai berikut: 
            """)
            st.markdown(rumus_basa_kuat(), unsafe_allow_html=True)
            st.markdown("""  
            Karakteristik Basa Kuat:
                        
            - **Ionisasi Lengkap:** Semua molekul basa terionisasi.
                        
            - **Kb Besar:** Nilai konstanta disosiasi basa (Kb) sangat besar.
                        
            - **Ph:** Larutan basa kuat memiliki pH yang sangat tinggi.
                        
            - **Kekuatan Reaksi:** Reaksi dengan asam menghasilkan garam dan air secara sempurna
            """)
        
        # Pilihan 3 / Keempat
        with tabs[3]:
            st.markdown('<h2><strong style="color: #E95793;">Basa Lemah</strong></h2>', unsafe_allow_html=True)

            st.markdown("""
            Basa Lemah: Basa lemah adalah basa yang hanya sebagian terionisasi dalam larutan air, yang berarti hanya sebagian kecil molekul basa melepaskan ion hidroksida (OH⁻) ke dalam larutan. Contoh basa lemah termasuk amonia (NH₃) dan metilamina (CH₃NH₂). Reaksi ionisasi basa lemah adalah sebagai berikut:
            """)
            st.markdown(rumus_basa_lemah(), unsafe_allow_html=True)
            st.markdown("""  
            Karakteristik Basa Lemah:
                        
            - **Ionisasi Parsial:** Hanya sebagian molekul basa terionisasi.
                        
            - **Kb Kecil:** Nilai konstanta disosiasi basa (Kb) kecil.
                        
            - **Ph:** Larutan basa lemah memiliki pH yang lebih rendah dibandingkan basa kuat dengan konsentrasi yang sama.
                        
            - **Kekuatan Reaksi:** Reaksi dengan asam menghasilkan garam dan air, tetapi tidak sepenuhnya.
            """)

    elif selected_calc_option == "Indikator":
        st.markdown('<h1 style="color: #DA0C81;">Penjelasan Indikator</h1>', unsafe_allow_html=True)
        tabs = st.tabs(['Sindur Metil (SM)', 'Indikator Metil Merah', 'Indikator Bromtimol Blue', 'Indikator Fenolftalein'])
        
        # Pilihan 0 / pertama
        # karena array dimulai dari 0 bukan 1
        with tabs[0]:
            st.markdown('<h2><strong style="color: #E95793;">Sindur Metil</strong></h2>', unsafe_allow_html=True)

            st.markdown("""
            Indikator Sindur Metil adalah senyawa kimia yang digunakan sebagai indikator pH pada larutan asam atau netral dalam rentang pH 3,1-4,4.
            berikut adalah beberapa fakta tentang sindur metil:
            
            - **Nama Kimia:** Sindur metil juga dikenal sebagai 4-dimetilaminoazobenzena atau merah CIB-3.
            
            - **Sifat Warna:** Senyawa ini memiliki sifat warna yang unik; berwarna merah dalam suasana asam dan berubah menjadi kuning dalam suasana basa.
            
            - **Indikator pH:** Sindur metil digunakan sebagai indikator pH dalam titrasi asam-basa. Perubahan warna yang ditunjukkan oleh sindur metil digunakan untuk menentukan titik akhir titrasi.
            
            - **Spektrum Absorpsi:** Sindur metil menunjukkan puncak absorpsi dalam spektrum UV-Vis pada panjang gelombang sekitar 520 nm.
            
            - **Aplikasi:** Selain sebagai indikator pH, sindur metil juga digunakan dalam pewarnaan histologi untuk mewarnai jaringan biologis dalam mikroskopi.
            
            - **Keamanan:** Meskipun digunakan dalam banyak aplikasi laboratorium, sindur metil harus ditangani dengan hati-hati karena sifatnya yang beracun dan kemungkinan pencemaran lingkungan.
            
            - **Penggunaan Historis:** Sindur metil telah digunakan dalam berbagai aplikasi sejak awal abad ke-20 dan tetap menjadi salah satu indikator pH yang penting dan umum digunakan hingga saat ini.
            """)
        
        # Pilihan 1 / kedua
        with tabs[1]:
            st.markdown('<h2><strong style="color: #E95793;">Indikator Metil Merah</strong></h2>', unsafe_allow_html=True)
            
            st.markdown("""        
            Indikator metil merah adalah senyawa kimia yang digunakan sebagai indikator pH pada larutan asam atau netral dalam rentang pH 4,2-6,3.
            berikut adalah beberapa fakta tentang indikator metil merah:
            
            - **Nama Kimia:** Metil merah juga dikenal sebagai p-[(dimetilamino)fenil]-diazenilbenzena atau C.I. 13020.
            
            - **Perubahan Warna:** Metil merah memiliki sifat warna yang unik: berwarna merah dalam suasana asam dan berubah menjadi kuning saat larutan menjadi basa. Perubahan warna ini terjadi di sekitar pH 4,4 hingga 6,2.
            
            - **Penggunaan:** Metil merah sering digunakan sebagai indikator pH dalam titrasi asam-basa, terutama dalam titrasi asam lemah dengan basa kuat atau dalam titrasi alkali dengan asam lemah.
            
            - **Titik Perubahan Warna:** Titik perubahan warna metil merah sedikit lebih rendah daripada fenolftalein, sehingga metil merah lebih cocok untuk titrasi asam yang lebih lemah.
            
            - **Kepekaan Terhadap Cahaya:** Metil merah rentan terhadap kerusakan oleh cahaya matahari dan sinar UV, sehingga harus disimpan dalam botol berwarna gelap untuk menjaga kestabilannya.
            """)
        
        # Pilihan 2 / ketiga
        with tabs[2]:
            st.markdown('<h2><strong style="color: #E95793;">Indikator Bromtimol Blue</strong></h2>', unsafe_allow_html=True)

            st.markdown("""        
            Indikator bromtimol blue adalah senyawa kimia yang digunakan sebagai indikator pH dalam titrasi asam-basa dalam rentang pH 6,0-7,6.
            berikut adalah beberapa fakta tentang indikator bromtimol blue:
            
            - **Nama Kimia:** Bromtimol blue juga dikenal sebagai 3',3'',5',5''-tetrabromofenolsulfonftalein atau C.I. 42090.
            
            - **Perubahan Warna:** Bromtimol blue memiliki sifat warna yang unik: berwarna biru dalam suasana basa, hijau dalam suasana netral, dan berubah menjadi kuning ketika larutan menjadi asam. Perubahan warna ini terjadi di sekitar pH 6,0 hingga 7,6.
            
            - **Kepekaan Terhadap Cahaya:** Seperti banyak indikator lainnya, bromtimol blue rentan terhadap kerusakan oleh cahaya matahari dan sinar UV, sehingga harus disimpan dalam botol berwarna gelap untuk menjaga kestabilannya.
            
            - **Penggunaan:** Bromtimol blue digunakan sebagai indikator pH dalam titrasi asam-basa, terutama dalam titrasi asam kuat dengan basa kuat atau dalam titrasi asam lemah dengan basa kuat.
            
            - **Penggunaan Lain:** Selain sebagai indikator pH, bromtimol blue juga digunakan dalam biologi sebagai penanda untuk mengidentifikasi zona pH dalam elektroforesis gel agarosa.
            """)
        
        # Pilihan 3 / Keempat
        with tabs[3]:
            st.markdown('<h2><strong style="color: #E95793;">Indikator Fenolftalein</strong></h2>', unsafe_allow_html=True)

            st.markdown("""        
            Indikator fenolftalein adalah senyawa kimia yang digunakan sebagai indikator pH dalam titrasi asam-basa dalam rentang pH 8,2-10.
            berikut adalah beberapa fakta tentang indikator fenolftalein:
            
            - **Nama Kimia:** Fenolftalein memiliki nama kimia 3,3-bis(4-hidroksifenil)-2H-isobenzofuran-1-on.
            
            - **Perubahan Warna:** Fenolftalein tidak berwarna dalam suasana asam, tetapi berubah menjadi merah muda hingga merah dalam suasana basa.
            
            - **Titik Perubahan Warna:** Perubahan warna fenolftalein terjadi di sekitar pH 8,2 hingga 10,0. Di bawah pH 8,2, fenolftalein tetap tidak berwarna, sedangkan di atas pH 10,0, fenolftalein menjadi merah.
            
            - **Penggunaan Umum:** Fenolftalein adalah indikator pH yang sangat umum digunakan dalam laboratorium kimia, terutama dalam titrasi asam-basa. Perubahan warna fenolftalein menunjukkan titik akhir titrasi, di mana asam dan basa telah bereaksi sepenuhnya.
            
            - **Kerusakan:** Fenolftalein rentan terhadap kerusakan oleh sinar UV dan dapat memudar dari paparan cahaya matahari yang berlebihan.
            """)

# Sistem pertama kali muncul
def main():
    st.sidebar.image("asset/icon.png", use_column_width=True)

    menu_option = st.sidebar.selectbox(
        'Pilih Menu:',
        ('Dashboard', 'Penjelasan', 'Kalkulator', 'Tentang Sistem', 'About Us')
    )
    if menu_option == 'Dashboard':
        dashboard()
    elif menu_option == 'Penjelasan':
        penjelasan()
    elif menu_option == 'Kalkulator':
        kalkulator()
    elif menu_option == 'Tentang Sistem':
        tentang_sistem()
    elif menu_option == 'About Us':
        about_us()

if __name__ == '__main__':
    main()
