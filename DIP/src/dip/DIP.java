
package dip;


import java.io.File;
import java.io.IOException;
import static java.lang.Thread.sleep;
import javafx.application.Application;
import javafx.embed.swing.SwingFXUtils;

import javafx.scene.Scene;
import javafx.scene.SnapshotParameters;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.image.WritableImage;
import javafx.stage.Stage;
import javax.imageio.ImageIO;


/**
 *
 * @author Martin
 */
public class DIP extends Application {
    public static void main(String[] args) {
            launch(args);
        }
        @Override
        public void start(Stage stage) throws Exception {
           //while(true){
             sleep(1000);
            //defining the axes
            final CategoryAxis xAxis = new CategoryAxis();
            final NumberAxis yAxis = new NumberAxis(0,30,3);
            //xAxis.setLabel("Uhrzeit");
            //creating the chart
            LineChart<String, Number> lineChart =
                    new LineChart<String, Number>(xAxis, yAxis);
            //lineChart.setTitle("Temperatur");
            //defining a series
            
                //sleep(1);
                XYChart.Series series = new XYChart.Series();
                series.setName("Temperatur");
                //populating the series with data
                series.getData().add(new XYChart.Data("7:00", 30));
                series.getData().add(new XYChart.Data("8:00", 14));
                series.getData().add(new XYChart.Data("9:00", 15));
                series.getData().add(new XYChart.Data("10:00", 24));
                series.getData().add(new XYChart.Data("11:00", 28));
                Scene scene = new Scene(lineChart, 520, 290);
                lineChart.setAnimated(false);
                lineChart.getData().add(series);
                lineChart.setStyle("-fx-font-size: " + 25 + "px;");            
                saveAsPng(lineChart, "/home/pi/Klassenklima/png/chart.png");
                System.out.println("Fertig");
            //}
            
        }
        public void saveAsPng(LineChart lineChart, String path) {
            WritableImage image = lineChart.snapshot(new SnapshotParameters(), null);
            File file = new File(path);
            try {
                ImageIO.write(SwingFXUtils.fromFXImage(image, null), "png", file);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
}
