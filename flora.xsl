<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="Flora">
    <html>
      <body>
        <h1>Flora's Data</h1>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th>num_register</th>
            <th>date</th>
            <th>author</th>
            <th>location</th>
            <th>UTM</th>
            <th>lithology</th>
            <th>coverage</th>
            <th>altitude</th>
            <th>plot_slope</th>
            <th>altitude_veg</th>
            <th>plot_area</th>
            <th>plot_orientation</th>
            <th>community</th>
            <th>abies_pinsapo</th>
            <th>pinus_halepensis</th>
            <th>juniperus_plumosa</th>
            <th>juniperus_oxycedrus</th>
            <th>ceratonia_siliqua</th>
            <th>chaualiop_limitis</th>
            <th>ranunculus_aqualitis</th>
            <th>acu_frentence</th>
            <th>sorbus_aria</th>
            <th>digitalis_obscura</th>
            <th>athamanta_vayredana</th>
            <th>centaurea_clementei</th>
            <th>campanula_mollis</th>
            <th>silene_andryalifolia</th>
            <th>sedum_dasphyllum</th>
            <th>chaenorrhinum_villosum</th>
            <th>rhamnus_myrtifolius</th>
            <th>teucrium_similatum</th>
            <th>cephalaria_leucantha</th>
            <th>helictotrichon_filifolium_arundanum</th>
            <th>thrincia_sp</th>
            <th>sanguisorba_minor</th>
            <th>scabiosa_turolensis_grosii</th>
          </tr>
          <xsl:for-each select="Data">
            <tr>
              <td>
                <xsl:value-of select="num_register"/>
              </td>
              <td>
                <xsl:value-of select="date"/>
              </td>
              <td>
                <xsl:value-of select="author" />
              </td>
              <td>
                <xsl:value-of select="location" />
              </td>
              <td>
                <xsl:value-of select="UTM" />
              </td>
              <td>
                <xsl:value-of select="lithology" />
              </td>
              <td>
                <xsl:value-of select="coverage" />
              </td>
              <td>
                <xsl:value-of select="altitude" />
              </td>
              <td>
                <xsl:value-of select="plot_slope" />
              </td>
              <td>
                <xsl:value-of select="altitude_veg" />
              </td>
              <td>
                <xsl:value-of select="plot_area" />
              </td>
              <td>
                <xsl:value-of select="plot_orientation" />
              </td>
              <td>
                <xsl:value-of select="community" />
              </td>
              <td>
                <xsl:value-of select="abies_pinsapo" />
              </td>
              <td>
                <xsl:value-of select="pinus_halepensis" />
              </td>
              <td>
                <xsl:value-of select="juniperus_plumosa" />
              </td>
              <td>
                <xsl:value-of select="juniperus_oxycedrus" />
              </td>
              <td>
                <xsl:value-of select="ceratonia_siliqua" />
              </td>
              <td>
                <xsl:value-of select="chaualiop_limitis" />
              </td>
              <td>
                <xsl:value-of select="ranunculus_aqualitis" />
              </td>
              <td>
                <xsl:value-of select="acu_frentence" />
              </td>
              <td>
                <xsl:value-of select="sorbus_aria" />
              </td>
              <td>
                <xsl:value-of select="digitalis_obscura" />
              </td>
              <td>
                <xsl:value-of select="athamanta_vayredana" />
              </td>
              <td>
                <xsl:value-of select="centaurea_clementei" />
              </td>
              <td>
                <xsl:value-of select="campanula_mollis" />
              </td>
              <td>
                <xsl:value-of select="silene_andryalifolia" />
              </td>
              <td>
                <xsl:value-of select="sedum_dasphyllum" />
              </td>
              <td>
                <xsl:value-of select="chaenorrhinum_villosum" />
              </td>
              <td>
                <xsl:value-of select="rhamnus_myrtifolius" />
              </td>
              <td>
                <xsl:value-of select="teucrium_similatum" />
              </td>
              <td>
                <xsl:value-of select="cephalaria_leucantha" />
              </td>
              <td>
                <xsl:value-of select="helictotrichon_filifolium_arundanum" />
              </td>
              <td>
                <xsl:value-of select="thrincia_sp" />
              </td>
              <td>
                <xsl:value-of select="sanguisorba_minor" />
              </td>
              <td>
                <xsl:value-of select="scabiosa_turolensis_grosii" />
              </td>
            </tr>
          </xsl:for-each>
          </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>