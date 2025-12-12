class TodoList {

    private static class Task {
        int id, userId, dueDate;
        String desc;
        List<String> tags;
        boolean done;

        Task(int id, int userId, String desc, int dueDate, List<String> tags) {
            this.id = id;
            this.userId = userId;
            this.desc = desc;
            this.dueDate = dueDate;
            this.tags = tags;
            this.done = false;
        }
    }

    private int nextId = 1;
    private final Map<Integer, Task> tasksById = new HashMap<>();
    private final Map<Integer, List<Task>> tasksByUser = new HashMap<>();

    public TodoList() {
        
    }
    
    public int addTask(int userId, String taskDescription, int dueDate, List<String> tags) {
        int id = nextId++;
        Task t = new Task(id, userId, taskDescription, dueDate, tags);

        tasksById.put(id, t);
        List<Task> list = tasksByUser.get(userId);
        if (list == null) {
            list = new ArrayList<>();
            tasksByUser.put(userId, list);
        }
        list.add(t);
        return id;
        
    }
    
    public List<String> getAllTasks(int userId) {
        List<Task> list = tasksByUser.get(userId);
        if (list == null) {
            return new ArrayList<>();
        }

        List<Task> pending = new ArrayList<>();
        for (Task t : list) {
            if (!t.done) {
                pending.add(t);
            }
        }
        pending.sort(Comparator.comparingInt(a -> a.dueDate));

        List<String> res = new ArrayList<>();
        for (Task t : pending) {
            res.add(t.desc);
        }
        return res;
    }
    
    public List<String> getTasksForTag(int userId, String tag) {
        List<Task> list = tasksByUser.get(userId);

        if (list == null) {
            return new ArrayList<>();
        }

        List<Task> pending = new ArrayList<>();

        for (Task t : list) {
            if (!t.done && t.tags.contains(tag)) {
                pending.add(t);
            }
        }

        pending.sort(Comparator.comparingInt(a -> a.dueDate));

        List<String> res = new ArrayList<>();
        for (Task t : pending) {
            res.add(t.desc);
        }
        return res;
    }
    
    public void completeTask(int userId, int taskId) {
        Task t = tasksById.get(taskId);
        if (t == null) {
            return;
        }
        if (t.userId != userId) {
            return;
        }
        if (t.done) {
            return;
        }
        t.done = true;
    }
}

/**
 * Your TodoList object will be instantiated and called as such:
 * TodoList obj = new TodoList();
 * int param_1 = obj.addTask(userId,taskDescription,dueDate,tags);
 * List<String> param_2 = obj.getAllTasks(userId);
 * List<String> param_3 = obj.getTasksForTag(userId,tag);
 * obj.completeTask(userId,taskId);
 */