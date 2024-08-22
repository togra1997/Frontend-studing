<script>
    let text = "";
    let todo_list = [];

    function addTodo(todo) {
        fetch("http://localhost:8000/todo", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                task: todo,
            }),
        })
            .then(() => {
                fetch("http://localhost:8000/todo")
                    .then(function (response) {
                        console.log(response);
                        return response.json();
                    })
                    .then(function (json) {
                        console.log(json);
                        todo_list = json;
                    });
            })
            .catch(() => {
                //スキップされる
            })
            .finally(() => {
                text = "";
                console.log("end"); //end
            });
    }
    function deleteTodo(id) {
        fetch("http://localhost:8000/todo/" + id, {
            method: "DELETE",
        }).then(() => {
            fetch("http://localhost:8000/todo")
                .then(function (response) {
                    console.log(response);
                    return response.json();
                })
                .then(function (json) {
                    console.log(json);
                    todo_list = json;
                });
        });
    }
</script>

<main>
    <h1>追加だけできるTODOアプリ</h1>
    <div class="field">
        <textarea bind:value={text}></textarea>
        <button on:click={() => addTodo(text)}>追加</button>
    </div>

    <div>
        <ul>
            {#each todo_list as todo}
                <li>
                    タスク{todo.id} - {todo.task}
                    <button on:click={() => deleteTodo(todo.id)}>削除</button>
                </li>
            {/each}
        </ul>
    </div>
</main>

<style>
    h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }
    .field {
        display: flex;
    }
</style>
