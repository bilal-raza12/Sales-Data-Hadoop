import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

public class SalesMapper extends Mapper<LongWritable, Text, Text, DoubleWritable> {
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        String line = value.toString();
        if (line.startsWith("ORDERNUMBER")) return;
        String[] cols = line.split(",");
        if (cols.length < 5) return;
        try {
            String productLine = cols[10].trim();
            double sales = Double.parseDouble(cols[3].trim());
            context.write(new Text(productLine), new DoubleWritable(sales));
        } catch (Exception e) {}
    }
}
