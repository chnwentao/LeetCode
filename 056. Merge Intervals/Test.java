class Interval {
	int start;
	int end;

	Interval() {
		start = 0;
		end = 0;
	}

	Interval(int s, int e) {
		start = s;
		end = e;
	}
}

public class Test {
    public static void main(String[] args){
        List<Interval> intervals = new ArrayList<Interval>();
        Interval i1 = new Interval(2, 3);
        intervals.add(i1);
        Interval i2 = new Interval(2, 2);
        intervals.add(i2);
        Interval i3 = new Interval(1, 3);
        intervals.add(i3);
        Interval i4 = new Interval(5, 7);
        intervals.add(i4);
        Interval i5 = new Interval(4, 6);
        intervals.add(i5);

        List<Interval> res = new ArrayList<Interval>();
        res = merge(intervals);

        for(Interval i : res){
            System.out.println("[" + i.start + "," + i.end + "]");
        }
    }

}
